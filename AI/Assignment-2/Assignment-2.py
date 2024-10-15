# -*- coding: utf-8 -*-
"""AI_Assignment2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FXxcpJOrbx8bl-xG_wZCV8th7iqt35PE
"""

# State is represented as (missionaries_left, cannibals_left, boat_position)
# boat_position = 1 means the boat is on the starting side, 0 means it's on the other side

# Function to check if the state is valid
def is_valid_state(state):
    missionaries_left, cannibals_left, _ = state
    missionaries_right = 3 - missionaries_left
    cannibals_right = 3 - cannibals_left

    # More cannibals than missionaries on either side is invalid
    if (missionaries_left > 0 and cannibals_left > missionaries_left) or \
       (missionaries_right > 0 and cannibals_right > missionaries_right):
        return False
    return True

# Function to generate all possible valid next states
def get_successors(state):
    successors = []
    missionaries_left, cannibals_left, boat_position = state
    boat_direction = -1 if boat_position == 1 else 1  # Boat moves to the opposite side

    # Possible moves (1 missionary, 1 cannibal), (2 missionaries), etc.
    possible_moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

    for missionaries, cannibals in possible_moves:
        new_missionaries_left = missionaries_left + boat_direction * missionaries
        new_cannibals_left = cannibals_left + boat_direction * cannibals
        new_state = (new_missionaries_left, new_cannibals_left, 1 - boat_position)
        if 0 <= new_missionaries_left <= 3 and 0 <= new_cannibals_left <= 3 and is_valid_state(new_state):
            successors.append(new_state)

    return successors

# Function to get user input for the next move
def get_user_input(state):
    print("\nCurrent state:")
    print(f"Missionaries Left: {state[0]}, Cannibals Left: {state[1]}, Boat on {'Left' if state[2] == 1 else 'Right'} Side")

    try:
        missionaries = int(input("Enter number of missionaries to move (0-2): "))
        cannibals = int(input("Enter number of cannibals to move (0-2): "))
    except ValueError:
        print("Invalid input. Please enter integers only.")
        return None

    if 0 <= missionaries <= 2 and 0 <= cannibals <= 2 and (missionaries + cannibals) > 0:
        return (missionaries, cannibals)
    else:
        print("Invalid move. Try again.")
        return None

# Main function to run the user-interactive version of the problem solver
def play_missionaries_and_cannibals():
    state = (3, 3, 1)  # Start with 3 missionaries, 3 cannibals, boat on starting side
    goal_state = (0, 0, 0)  # Goal is to get everyone across with boat on the other side

    visited = set([state])  # Keep track of visited states

    while state != goal_state:
        move = None
        while move is None:
            move = get_user_input(state)

        missionaries, cannibals = move
        boat_direction = -1 if state[2] == 1 else 1
        new_state = (
            state[0] + boat_direction * missionaries,
            state[1] + boat_direction * cannibals,
            1 - state[2]
        )

        if 0 <= new_state[0] <= 3 and 0 <= new_state[1] <= 3 and is_valid_state(new_state):
            state = new_state
            if state == goal_state:
                print("\nCongratulations! You've successfully moved all missionaries and cannibals to the other side!")
                break
            visited.add(state)
        else:
            print("Invalid move. The state is either not allowed or violates the problem constraints. Try again.")

    if state != goal_state:
        print("\nGame Over. Better luck next time!")

# Start the game
play_missionaries_and_cannibals()