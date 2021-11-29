from game_of_life import next_board_state

# DONE: there's a lot of repeated code here. Can you move some of into reusablefunctions to make it shorter and neater?
def compare(expected_state, actual_state, state_name):
    if expected_state == actual_state:
        print(f"PASSED {state_name}")
    else:
        print("FAILED 1!")
        print("EXPECTED:")
        print(expected_state)
        print("ACTUAL")
        print(actual_state)

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors should stay dead
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    actual_next_state1 = next_board_state(init_state1)

    compare(expected_next_state1, actual_next_state1, "1")

    # TEST 2: dead cells with exactly 3 neighbors should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]

    actual_next_state2 = next_board_state(init_state2)

    compare(actual_next_state2, actual_next_state2, "2")


    # TEST 3: live cells with more than 3 neighbors should come dead.
    init_state3 = [
        [1,0,1],
        [0,1,0],
        [1,1,0]
    ]
    expected_next_state3 = [
        [0,1,0],
        [0,0,1],
        [1,1,0]
    ]

    actual_next_state3 = next_board_state(init_state3)

    compare(expected_next_state3, actual_next_state3, "3")

    # TEST 4: live cells with 2 or 3 neighbors should stay alive.
    init_state4 = [
        [1,0,1],
        [0,1,0],
        [0,0,0]
    ]
    expected_next_state4 = [
        [0,1,0],
        [0,1,0],
        [0,0,0]
    ]

    actual_next_state4 = next_board_state(init_state4)

    compare(expected_next_state4, actual_next_state4, "4")

    # TEST 5: live cells with 0 or 1 neighbors should come dead.
    init_state5 = [
        [1,0,0],
        [1,0,0],
        [0,0,0]
    ]
    expected_next_state5 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    actual_next_state5 = next_board_state(init_state5)

    compare(expected_next_state5, actual_next_state5, "5")