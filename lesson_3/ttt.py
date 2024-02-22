import random

def initialize_board():
    INITIAL_MARKER = ' '
    return {square: INITIAL_MARKER for square in range(1,10)}

def display_board(board):
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

def available_squares():
    return [k for k, v in board.items() if v == ' ']


def valid_input(user_input):
    try:
        int(user_input)
    except ValueError:
        return False
    else:
        return True

def player_chooses_square():
    PLAYER_MARKER = 'X'
    available_choices = available_squares()
    player_choice = input(f'Please choose from the avaiable squares: {available_choices} ')

    while not valid_input(player_choice) or int(player_choice) not in available_choices:
        player_choice = input(f'Invalid input. Please choose from: {available_choices} ')

    board[int(player_choice)] = PLAYER_MARKER

def computer_chooses_square():
    COMPUTER_MARKER = 'O'
    available_choices = available_squares()
    computer_choice = random.choice(available_choices)

    board[computer_choice] = COMPUTER_MARKER

board = initialize_board()

while True:
    display_board(board)
    player_chooses_square()
    computer_chooses_square()
    display_board(board)
