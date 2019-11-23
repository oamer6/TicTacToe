# ------- Global Variables -----------

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Who's turn is it
current_player = "X"


# Display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game of Tic Tac Toe
def play_game():
    # Display initial board
    display_board()

    while game_still_going:
        # Handle a single turn
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip to the other player
        flip_player()

        # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# Handle a turn
def handle_turn(player):
    print(player + "'s turn.")
    position = input("Choose a position 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Try again.")

    board[position] = player

    display_board()


# Check if the game is over
def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    # Set up global variables
    global winner

    # check rows
    row_winner = check_rows()
    # check cols
    column_winner = check_cols()
    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
    elif diagonal_winner:
        # there was a win
        winner = diagonal_winner
    else:
        # there was no win
        winner = None
    return


def check_rows():
    # Set up global variables
    global game_still_going

    # Check if rows have all similar values
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match, flag the win
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_cols():
    # Set up global variables
    global game_still_going

    # Check if rows have all similar values
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any row does have a match, flag the win
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # Set up global variables
    global game_still_going

    # Check if rows have all similar values
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    # If any row does have a match, flag the win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # Global variables
    global current_player
    # If the current player was X, switch it to O
    if current_player == "X":
        current_player = "O"

    # If the current player was X, switch it to O
    elif current_player == "O":
        current_player = "X"
    return


play_game()

# board
# display board
# play the game
# handle turn
# check win
# check rows
# check cols
# check diagonals
# check tie
# flip player