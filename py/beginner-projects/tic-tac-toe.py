import sys
import random

def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-' * 5)
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-' * 5)
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

def get_computer_move(board):
    moves = []
    for key, value in board.items():
        if value == ' ':
            moves.append(key)
    return random.choice(moves)

def win_check(board):
    moves = list(board.values())
    converted_moves = []
    for y in range(0 , len(moves), 3):
        temp_lst = []
        for x in range(3):
            temp_lst.append(moves[x + y])
        converted_moves.append(temp_lst)

    for y in range(len(converted_moves)):
        if converted_moves[y][0] and converted_moves[y][1] and converted_moves[y][2] == 'O':




game_board = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
               'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
               'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

player_char = 'O'
computer_char = 'X'


print_board(game_board)
while True:
    print('Where you want to move? ', end='')
    player_move = input()
    if player_move in game_board and game_board[player_move] == ' ':
        game_board[player_move] = player_char
        computer_move = get_computer_move(game_board)
        game_board[computer_move] = computer_char
        print_board(game_board)
        win_check(game_board)
    else:
        print('You can\'t make move here.')