# --Global vars--


# Game board
board = ["-", "-", " -",
         "-", "-", " -",
         "-", "-", " -"]

# if game is still going
game_still_going = True

# who won or tie

winner = None

# who's turn is it?

current_player = 'X'


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    # display initial board
    display_board()

    # while game is still going
    while game_still_going:
        # handle a single turn
        handle_turn(current_player)
        # check if game has ended
        check_if_game_over()
        # Flip to the other player
        flip_player()

    # the game has ended
    if winner == 'X' or winner == 'O':
        print(winner + ' won.')
    elif winner is None:
        print('Tie')


# handle a single turn
def handle_turn(player):
    position = input('Choose a position from 1 to 9:')
    position = int(position) - 1
    board[position] = "X"
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    # set global vars
    global winner

    # check rows
    row_winner = check_rows()
    print(row_winner)

    # check columns
    column_winner = check_columns()
    print(column_winner)
    # check diagonal
    diagonal_winner = check_diagonals()
    print(diagonal_winner)
    if row_winner:
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
    elif diagonal_winner:
        # there was a win
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():

    # set global vars
    global game_still_going
    # check if rows have all same values and not empty
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"
    # return the winner (X or O)
    if row1 or row2 or row3:
        game_still_going = False
        print(game_still_going)
    if row1:
        return board[0]
    if row2:
        return board[3]
    if row3:
        return board[6]
    return


def check_columns():
    # set global vars
    global game_still_going
    # check if columns have all values and not empty
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'
    # return the winner (X or O)
    if column1 or column2 or column3:
        game_still_going = False
    if column1:
        return board[0]
    if column2:
        return board[1]
    if column3:
        return board[2]
    return


def check_diagonals():
    # set global vars
    global game_still_going
    # check if diagonals have all values and not empty
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[6] == board[4] == board[2] != '-'
    # return the winner (X or O)
    if diagonal1 or diagonal2:
        game_still_going = False
    if diagonal1:
        return board[0]
    if diagonal2:
        return board[6]

    return


def check_if_tie():
    return


def flip_player():
    # flip from X to O
    return


play_game()
# display board
# play game
# handle turn
# #heck win
# check rows
# check columns
# check diagonal
# check tie
# flip player
