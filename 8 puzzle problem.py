from collections import deque

class Puzzle:
    def __init__(self, board, moves=0, parent=None):
        self.board = board
        self.moves = moves
        self.parent = parent
        self.zero_position = self.find_zero_position()

    def find_zero_position(self):
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                if value == 0:
                    return (i, j)
    
    def get_possible_moves(self):
        i, j = self.zero_position
        moves = []

        if i > 0:  # Move up
            moves.append((i - 1, j))
        if i < 2:  # Move down
            moves.append((i + 1, j))
        if j > 0:  # Move left
            moves.append((i, j - 1))
        if j < 2:  # Move right
            moves.append((i, j + 1))

        return moves

    def generate_new_state(self, new_zero_position):
        i, j = self.zero_position
        new_i, new_j = new_zero_position

        # Swap zero with the target position
        new_board = [row[:] for row in self.board]
        new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]

        return Puzzle(new_board, self.moves + 1, self)

    def is_goal(self):
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def print_path(self):
        path = []
        state = self
        while state:
            path.append(state)
            state = state.parent
        path.reverse()

        for state in path:
            for row in state.board:
                print(row)
            print()

def bfs_solve(start_board):
    start_state = Puzzle(start_board)
    if start_state.is_goal():
        return start_state

    frontier = deque([start_state])
    explored = set()

    while frontier:
        state = frontier.popleft()
        explored.add(state)

        for move in state.get_possible_moves():
            new_state = state.generate_new_state(move)

            if new_state not in explored and new_state not in frontier:
                if new_state.is_goal():
                    return new_state
                frontier.append(new_state)
    return None

def get_user_input():
    print('Enter the numbers for the 8-puzzle, row by row (use 0 for the empty space):\n')
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            while True:
                try:
                    num = int(input(f"Enter number for position ({i}, {j}): "))
                    if 0 <= num <= 8:
                        row.append(num)
                        break
                    else:
                        print("Please enter a number between 0 and 8.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        board.append(row)
    return board

start_board = get_user_input()
solution = bfs_solve(start_board)
if solution:
    print("Solution found in", solution.moves, "moves:")
    solution.print_path()
    
else:
    print("No solution found.")
