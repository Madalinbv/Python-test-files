# board
# display board
# play game
# check win
# check row
# check column
# check diagonals
# check tie
# flip player

# -----Global Variables ----------

# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# If game is still going
game_still_going = True


# who won ? or tie ?
winner = None

# who's turn is it
current_player = "X"


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

    # displaying the board first
    display_board()

    # while the game is still going
    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # flip to the other player
        flip_player()

        # check if the game has ended
        check_if_game_over()


# The game has ended
    if winner == "X" or winner == "0":
        print(winner + " won.")
    elif winner is None:
        print("Tie.")


# handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1 to 9 :")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input.\nChoose a position from 1 to 9:")

        position = int(position)-1

        if board[position] == "-":
            #  valid = True
            break
        else:
            print("You can't go there.Go again.\n")

    board[position] = player
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    # set up global winner
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
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
        winner = None


def check_rows():
    # set up global variable
    global game_still_going

    # check if any of the rows have all the same values (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match, flag that there is a win.
    if row_1 or row_2 or row_3:
        game_still_going = False
        # Return the winner (X or 0)
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]


def check_columns():
    # set up global variable
    global game_still_going

    # check if any of the columns have all the same values (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column does have a match, flag that there is a win.
    if column_1 or column_2 or column_3:
        game_still_going = False
        # Return the winner (X or 0)
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]


def check_diagonals():
    # set up global variable
    global game_still_going

    # check if any of the columns have all the same values (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # If any column does have a match, flag that there is a win.
    if diagonal_1 or diagonal_2:
        game_still_going = False
        # Return the winner (X or 0)
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False


def flip_player():
    # global variables we need
    global current_player
    if current_player == "X":
        current_player = "0"
    elif current_player == "0":
        current_player = "X"


play_game()
