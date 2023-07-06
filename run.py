from random import randint


def board():
    return [['~'for x in range(8)] for y in range (8)]
    for b in board:
        print(*b)

def player_board(board):
    for b in board:
        print(*b)
    
player_board(board)