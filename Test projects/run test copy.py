#Random module for randomly accepting the values
# ‘X’ indicates the ships hit
# ‘-‘ indicates the hits missed
from random import randint

num = 8

Hidden_Pattern=[['~'for x in range(num)] for y in range (num)]
Guess_Pattern=[['~'for x in range(num)] for y in range (num)]

let_to_num={'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}

def print_board(board):
    print(' A B C D E F G H')
    print(' ***************')
    row_num=1
    space = ''
    for row in i(len(board)):
        space+=" ".join(board[i])+'\n'
    return(space)


print(print_board(Guess_Pattern))