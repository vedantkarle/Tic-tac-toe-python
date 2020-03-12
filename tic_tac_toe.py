import random


def display_board(board):
    print(board[7], end=" ")
    print('|', end=" ")
    print(board[8], end=" ")
    print('|', end="")
    print(board[9])
    print('---------')
    print(board[4], end=" ")
    print('|', end=" ")
    print(board[5], end=" ")
    print('|', end="")
    print(board[6])
    print('---------')
    print(board[1], end=" ")
    print('|', end=" ")
    print(board[2], end=" ")
    print('|', end="")
    print(board[3])


def player_input():
    marker = ' '

    while marker != 'X' and marker != 'O':
        marker = input(' Player1 : Choose X or O: ').upper()
    if marker == 'X':
        return('X', 'O')
    else:
        return('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or  # rows
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[1] == board[4] == board[7] == mark) or  # columns
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[1] == board[5] == board[9] == mark) or  # diagonals
            (board[1] == board[5] == board[7] == mark))


def choose_player():
    flip = random.randint(0, 1)

    if flip == 0:
        return 'Player1'
    else:
        return 'Player2'


def check_space(board, position):
    return board[position] == ' '


def full_board_check(board):
    for i in range(9):
        # i=position and if this returns true i.e. space is available then function returns false
        if check_space(board, i):
            return False
        else:
            return 'The board is full'


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not check_space(board, position):
        position = int(input(" Choose a position from (1-9): "))
    return position


def replay():
    choice = input(" Want to play again ? Choose Yes or No: ")
    return choice == 'Yes'


print("Welcome to Tic-Tac-Toe")
# star the game
while True:
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    # choosing player to go first
    turn = choose_player()
    print(turn + ' will go first ')

    play_game = input(' Ready to play ? y or n: ')
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

# begin the game
    while game_on:
        if turn == 'Player1':
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # Place the marker in that position
            place_marker(the_board, player1_marker, position)
            # Check if won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print(' Player1 has won!!! ')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    break
                else:
                    turn = 'Player2'

        else:
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # Place the marker in that position
            place_marker(the_board, player2_marker, position)
            # Check if won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player2 has won!!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME")
                    break
                else:
                    turn = 'Player1'

    if not replay():
        break
