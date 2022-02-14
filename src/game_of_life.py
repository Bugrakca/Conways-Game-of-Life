import random, time
# TODO: Research and implement Langton’s Ant
# TODO: Research and implement Brian’s Brain
# TODO: Research and implement Day and Night
# TODO: Make a command line tool that allows the user to choose which of your cellular automa they would like to run
# TODO: Implement the terminal UI using curses

def dead_state(width, height):
    '''Dead state of the board with all zeros'''
    # board_state = list()
    # for y in range(height):
    #     inner_list = list()
    #     for x in range(width):
    #         inner_list.append(0)
    #     board_state.append(inner_list)
    return [[0 for x in range(width)]for y in range(height)]

def random_state(width, height):
    '''Creates a state where each cell is randomly generated.

    Parameters
    -----------
    width: width of the state
    height: height of the state

    Returns
    -----------
    State of randomly generated ones and zeros'''

    state = dead_state(width, height)
    for x in range(len(state)):# This is the y coordinates
        for y in range(len(state[0])):
            random_number = random.random()
            if random_number <= 0.5:
                state[x][y] = 0
            else:
                state[x][y] = 1
    return state

def render(state):
    '''Turning ones and zeros into ascii characters and printing out to the
terminal.

    Parameters
    -----------
    state: a game state

    Returns
    -----------
    Nothing - this is just a display function.'''
    for x in range(len(state)): # This is the y coordinates
        print("|", end="")
        for y in range(len(state[0])):
            if state[x][y] == 0:
                print(" ", end=" ")
            else:
                print("#", end=" ")
        print("|", end=" ")
        print()

def next_board_state(state):
    '''Creating a next board state with given state

    Parameters
    ----------
    state: game state

    Returns
    -------
    Returns the next state of the game'''
    width = len(state[0])
    height = len(state)
    next_state = dead_state(width,height)

    for x in range(height):
        for y in range(width):
            next_state[x][y] = next_cell_coord((x, y), state)
    return next_state

def next_cell_coord(next_coords, state):
    '''Getting a next cell coordinates by the rules.

    Parameters
    ----------
    next_coords: Tuple coordinates
    state: current state of the game

    Returns
    --------
    Returning the next_coords - tuple (x, y)'''
    i = next_coords[0]
    j = next_coords[1]
    count = 0

    for x in range((i-1), (i+1)+1):
        if x < 0 or x >= len(state):
            continue
        for y in range((j-1), (j+1)+1):
            if y < 0 or y >= len(state[0]):
                continue
            if x == i and y == j:
                continue
            if state[x][y] == 1:
                count += 1

    if state[i][j] == 1:
        if count <= 1:
            return 0
        elif count <= 3:
            return 1
        else:
            return 0
    else:
        if count == 3:
            return 1
        else:
            return 0

def load_board_state(file_name):
    state = list()
    with open(file_name, "r") as f:
        for line in f:
            line = line.rstrip('\n')
            x = [int(a) for a in str(line)]
            state.append(x)
    return state

def forever(state):
    '''Runs the game of life forever.

    Parameters
    -----------
    state: the game state

    Returns
    --------
    This function never returns - the program must be forcibly exited!'''
    initial_state = state
    while True:
        render(next_board_state(initial_state))
        initial_state = next_board_state(initial_state)
        time.sleep(0.03)
if __name__ == "__main__":
    # for i in random_state(3,3):
    #     print(i)
    # render(random_state(20,30))
    # next_board_state(random_state(3,3))
    # forever(random_state(20,30))
    forever(load_board_state("./glider_gun.txt"))
