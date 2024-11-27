import math

# Define players
PLAYER_X = 'X'  # AI player
PLAYER_O = 'O'  # User
EMPTY = ' '     # Empty cell

# Define a function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if there's a winner or if the board is full
def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for player in [PLAYER_X, PLAYER_O]:
        # Check rows and columns
        for i in range(3):
            if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
                return player
        # Check diagonals
        if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
            return player

    # Check for a draw (no empty cells)
    if all(cell != EMPTY for row in board for cell in row):
        return "Draw"

    return None

# Minimax algorithm implementation
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == PLAYER_X:
        return 1  # AI wins
    elif winner == PLAYER_O:
        return -1  # User wins
    elif winner == "Draw":
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    score = minimax(board, depth + 1, False)
                    board[i][j] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    score = minimax(board, depth + 1, True)
                    board[i][j] = EMPTY
                    best_score = min(score, best_score)
        return best_score

# Function to find the best move for the AI
def find_best_move(board):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                score = minimax(board, 0, False)
                board[i][j] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Main game loop
def play_game():
    board = [[EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY],
             [EMPTY, EMPTY, EMPTY]]

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O' and the AI is 'X'.")
    print_board(board)

    while True:
        # User's turn
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2) for your move: "))
                col = int(input("Enter the column (0, 1, or 2) for your move: "))
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER_O
                    break
                else:
                    print("That cell is already taken. Choose another one.")
            except (ValueError, IndexError):
                print("Invalid input. Enter a number between 0 and 2.")

        print("Your move:")
        print_board(board)

        # Check for a winner after the user's move
        winner = check_winner(board)
        if winner:
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        # AI's turn
        print("AI is making its move...")
        ai_move = find_best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = PLAYER_X
            print_board(board)
        else:
            print("No moves left!")
            break

        # Check for a winner after the AI's move
        winner = check_winner(board)
        if winner:
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

# Start the game
play_game()
