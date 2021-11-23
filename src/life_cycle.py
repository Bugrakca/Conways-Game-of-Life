import random
'''
Rules
1. Play proceeds in rounds. During each round, each cell looks at its 8
   immediate neighbors and counts up the number of them that are currently
   alive.
    a. Any live cell with 0 or 1 live neighbors becomes dead, because of
    underpopulation
    b. Any live cell with 2 or 3 live neighbors stay alive, because its
    neighborhood is just right.
    c. Any live cell with more than 3 live neighbors becomes dead, because of
    overpopulation.
    d. Any dead cell with exactly 3 live neighbors becomes alive, by
    reproduction.
'''

#* Create a method to retunr the empty board.
def death_state(widht, height):
    death_board = list()
    for x in range(height):
        death_board.append(list())
        for y in range(widht):
            death_board[x].append(0)
    return death_board

#* Create a method to return the board.
def board_state(widht=11, height=11):
    '''Create a 2d board with one(1)s and zero(0)s. 1 is Alive, 0 is Dead'''
    # board_state = list()
    # for x in range(height):
    #     board_state.append(list())
    #     for y in range(widht):
    #         board_state[x].append(random.randint(0,1))
    # return board_state
    state = death_state(widht, height)
    for x in state:
        for y in range(len(x)):
            random_number = random.random()
            if random_number >= 0.5:
                x[y] = 0
            else:
                x[y] = 1
    return state

for i in board_state(20, 30):
    print(i)