from random import randint
import time

num = 8

Hidden_Pattern=[['~'for x in range(num)] for y in range (num)]
Guess_Pattern=[['~'for x in range(num)] for y in range (num)]


def create_board(board):
   
    space = ''
    for i in range (len(board)):
        space+=" ".join(board[i])+'\n'
    return(space)


print("\nWELCOME TO BATTLESHIP")
print("\nAn enemy fleet is spotted on the horizon.")
print("You have 10 missiles at your disposal.")
print("Try to sink all their ships before it's too late.\n")
time.sleep(5)
print("\nCan you guess where on the board the 6 hidden ships are?")
print(create_board(Guess_Pattern))
    