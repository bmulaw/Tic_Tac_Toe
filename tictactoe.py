board = ['-','-','-',
        '-', '-', '-',
        '-', '-', '-']
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

game_still_going = True
winner = None
curr_player = "X"

def play_game():
    display_board()
    while game_still_going:
        handle_turn(curr_player)
        check_game_over()
        flip_player()
    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Tie.")

def flip_player():
    global curr_player
    if curr_player == "X":
        curr_player = "O"
    elif curr_player == "O":
        curr_player = "X"
    return curr_player

def handle_turn(curr_player):
    print(curr_player +"'s turn...")
    position = input("Chose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Please try again. Chose a position from 1-9: ")
        position = int(position) -1
        if board[position] == "-":
            valid = True
        else:
            print("Opps, that spot is already taken. Please try a different")
    board[position] = curr_player
    display_board()

def check_game_over():
    check_for_winner()
    check_if_tie() 

def check_for_winner():
    global winner
    row_winner = check_row()
    colm_winner = check_colm()
    diag_winner = check_diag()
    if row_winner:
        winner = row_winner
    elif colm_winner:
        winner = colm_winner
    elif diag_winner:
        winner = diag_winner
    else:
        winner = None 

def check_row():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_colm():
    global game_still_going
    colm_1 = board[0] == board[3] == board[6] != "-"
    colm_2 = board[1] == board[4] == board[7] != "-"
    colm_3 = board[2] == board[5] == board[8] != "-"
    if colm_1 or colm_2 or colm_3:
        game_still_going = False
    if colm_1:
        return board[0]
    elif colm_2:
        return board[1]
    elif colm_3:
        return board[2]

def check_diag():
    global game_still_going
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[2] == board[4] == board[6] != "-"
    if diag_1 or diag_2:
        game_still_going = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[2]


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False






play_game()