import random, os

INITIAL_MARKER = ' '
PLAYER_MARKER = 'X'
COMPUTER_MARKER = 'O'


def initialize_board():
    return {square: INITIAL_MARKER for square in range(1,10)}

def display_board(board):
    #os.system('clear')
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def available_squares(board):
    return [k for k, v in board.items() if v == INITIAL_MARKER]

def valid_input(user_input):
    try:
        int(user_input)
    except ValueError:
        return False
    else:
        return True

def player_chooses_square(board):
    available_choices = available_squares(board)
    player_choice = input(f'Please choose from the avaiable squares: {available_choices} ')

    while not valid_input(player_choice) or int(player_choice) not in available_choices:
        player_choice = input(f'Invalid input. Please choose from: {available_choices} ')

    board[int(player_choice)] = PLAYER_MARKER

def computer_chooses_square(board):
    available_choices = available_squares(board)
    if not len(available_choices):
        return
    
    computer_choice = random.choice(available_choices)

    board[computer_choice] = COMPUTER_MARKER

def is_full(board):
    return not len(available_squares(board))

def detect_winner(board):
    WINNING_PATTERNS = [
        [1,2,3], [4,5,6], [7,8,9], # HORIZONTAL
        [1,4,7], [2,5,8], [3,6,9], # VERTICAL
        [1,5,9], [3,5,7],          # DIAGONAL
    ]

    for pattern in WINNING_PATTERNS:
        if all([board[square] == PLAYER_MARKER for square in pattern]):
            return 'Player'
        if all([board[square] == COMPUTER_MARKER for square in pattern]):
            return 'Computer'
            
    return None

board = initialize_board()

while True:
    display_board(board)
    player_chooses_square(board)
    computer_chooses_square(board)
    display_board(board)
    if is_full(board) or detect_winner(board):
        print('THE BOARD IS FULL')
        break
