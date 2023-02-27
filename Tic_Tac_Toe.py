def print_board(board):
    """
    This function prints the current state of the board.
    """
    print("   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")


def check_win(board, player):
    """
    This function checks if the player has won the game.
    """
    win_conditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def play_game():
    """
    This function runs the game.
    """
    print("Welcome to Tic Tac Toe!")
    print("Player 1 will be X, and Player 2 will be O.")
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        move = int(input(f"{current_player}, enter your move (1-9): ")) - 1
        if board[move] != " ":
            print("That space is already taken. Please choose another.")
            continue
        board[move] = current_player
        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            game_over = True
        elif " " not in board:
            print_board(board)
            print("It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"


play_game()
