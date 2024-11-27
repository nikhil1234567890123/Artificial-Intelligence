import heapq

class PuzzleState:
    def __init__(self, board, parent=None, move=None, depth=0):
        self.board = board
        self.parent = parent
        self.move = move
        self.depth = depth
        self.zero_pos = board.index(0)  # Find the position of the zero tile (empty space)

    def __lt__(self, other):
        # Comparison function for priority queue (based on total cost)
        return self.total_cost() < other.total_cost()

    def is_goal_state(self):
        # Check if the current board configuration is the goal state
        return self.board == [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def get_possible_moves(self):
        # Find the possible moves from the current state
        moves = []
        x, y = divmod(self.zero_pos, 3)  # Get row (x) and column (y) of the zero tile

        # Append valid moves: (row change, column change)
        if x > 0: moves.append((-1, 0))  # Move up
        if x < 2: moves.append((1, 0))   # Move down
        if y > 0: moves.append((0, -1))  # Move left
        if y < 2: moves.append((0, 1))   # Move right

        return moves

    def move_tile(self, direction):
        # Create a new board by moving the zero tile in the specified direction
        new_board = self.board[:]
        x, y = divmod(self.zero_pos, 3)
        dx, dy = direction
        new_zero_pos = (x + dx) * 3 + (y + dy)
        new_board[self.zero_pos], new_board[new_zero_pos] = new_board[new_zero_pos], new_board[self.zero_pos]
        return PuzzleState(new_board, self, direction, self.depth + 1)

    def total_cost(self):
        # Calculate total cost: depth (g) + heuristic (h), where h is Manhattan distance + misplaced tiles
        return self.depth + self.manhattan_distance() + self.misplaced_tiles()

    def misplaced_tiles(self):
        # Calculate the number of misplaced tiles (ignore the zero tile)
        return sum(1 for i in range(9) if self.board[i] != 0 and self.board[i] != i + 1)

    def manhattan_distance(self):
        # Calculate Manhattan distance of the board configuration
        distance = 0
        for i in range(9):
            if self.board[i] != 0:
                x, y = divmod(i, 3)  # Current position
                goal_x, goal_y = divmod(self.board[i] - 1, 3)  # Goal position
                distance += abs(x - goal_x) + abs(y - goal_y)
        return distance

def solve_puzzle(initial_board):
    start_state = PuzzleState(initial_board)
    open_queue = []
    heapq.heappush(open_queue, start_state)
    closed_set = set()

    while open_queue:
        current_state = heapq.heappop(open_queue)

        if current_state.is_goal_state():
            return reconstruct_solution(current_state)

        closed_set.add(tuple(current_state.board))

        for move in current_state.get_possible_moves():
            neighbor_state = current_state.move_tile(move)

            if tuple(neighbor_state.board) in closed_set:
                continue

            heapq.heappush(open_queue, neighbor_state)

    return None

def reconstruct_solution(state):
    # Reconstruct the path of moves by backtracking through the parent nodes
    moves = []
    while state.parent:
        moves.append(state.move)
        state = state.parent
    return moves[::-1]  # Return the moves in reverse order

def input_puzzle():
    print("Enter the puzzle configuration (0 for the empty space).")
    board = []
    
    while True:
        board = []
        try:
            for i in range(3):
                row = input(f"Enter row {i + 1} (space-separated): ").split()
                board.extend(map(int, row))  # Convert input to integers
            
            # Ensure the board contains exactly 9 elements
            if len(board) != 9:
                raise ValueError("The puzzle must have exactly 9 tiles.")
            
            # Ensure the board contains exactly one 0
            if board.count(0) != 1:
                raise ValueError("The puzzle must contain exactly one empty tile (0).")
            
            break  # Break loop if input is valid
        
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.")
    
    return board

def format_moves(moves):
    directions = {
        (-1, 0): "Up",
        (1, 0): "Down",
        (0, -1): "Left",
        (0, 1): "Right"
    }
    return [directions[move] for move in moves]

if __name__ == "__main__":
    initial_board = input_puzzle()
    solution = solve_puzzle(initial_board)

    if solution:
        print("\nSolution found!")
        print("Moves to solve the puzzle:")
        formatted_moves = format_moves(solution)
        for index, move in enumerate(formatted_moves, 1):
            print(f"Move {index}: {move}")
        print(f"\nTotal moves: {len(solution)}")
    else:
        print("\nNo solution exists for the given puzzle configuration.")
