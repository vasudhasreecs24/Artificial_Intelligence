# 8-Puzzle using Depth First Search (DFS)


# Function to print the puzzle
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i + 1], state[i + 2])
    print()


# Function to generate valid neighboring states
def get_neighbors(state):

    neighbors = []

    # Find position of blank space (0)
    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    # Possible moves: UP, DOWN, LEFT, RIGHT
    moves = [
        (-1, 0),   # UP
        (1, 0),    # DOWN
        (0, -1),   # LEFT
        (0, 1)     # RIGHT
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        # Check whether the move is valid
        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            # Create a copy of the state
            new_state = list(state)

            # Swap blank with the adjacent tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            # Convert list back to tuple
            neighbors.append(tuple(new_state))

    return neighbors


# DFS function
def dfs_8_puzzle(initial, goal):

    # Stack contains:
    # (current state, path taken to reach the state)
    stack = [(initial, [initial])]

    # Mark initial state as visited
    visited = {initial}

    while stack:

        # Remove top element from stack
        state, path = stack.pop()

        # Check whether goal is reached
        if state == goal:
            return path

        # Generate all possible next states
        for new_state in get_neighbors(state):

            # Visit only unvisited states
            if new_state not in visited:

                visited.add(new_state)

                # Add new state and updated path to stack
                stack.append(
                    (new_state, path + [new_state])
                )

    # No solution found
    return None


# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

# Initial state
initial = (
    1, 2, 3,
    4, 5, 6,
    7, 0, 8
)

# Goal state
goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)


# Display initial state
print("Initial State:")
print_puzzle(initial)

# Display goal state
print("Goal State:")
print_puzzle(goal)


# Run DFS
solution = dfs_8_puzzle(initial, goal)


# Display solution
if solution:

    print("Solution Found!")

    print("Number of moves:", len(solution) - 1)

    print("\nSteps:")

    for i, state in enumerate(solution):

        print("Step", i)
        print_puzzle(state)

else:

    print("FAILURE: No solution found.")