"""
Import random module for random placement of ships.
Import time module to create delays.
"""
from random import randint
import time

num = 8

# Hidden board for random ship placement.
Hidden_Pattern = [['~'for x in range(num)] for y in range(num)]
# Guess board that shows guessses.
Guess_Pattern = [['~'for x in range(num)] for y in range(num)]


# Creates a board grid layout with spaces in between.
def create_board(board):
    space = ''
    for i in range(len(board)):
        space += " ".join(board[i])+'\n'
    return (space)


# Function for guessing where on the board the hidden ships are
def guess_ship_location():
    try:
        row = int(input("Please enter a row number 0-7:"))
        while row not in range(8):
            print('That is not a valid row number')
            row = int(input("Please enter a row number 0-7:"))
        column = int(input("Write a column number 0-7:"))
        while column not in range(8):
            print('That is not a valid column number')
            column = int(input("Write a column number 0-7:"))
        return int(row), int(column)
    except ValueError:
        print("Invalid input. Please enter a single digit.")
        return guess_ship_location()


# Function that randomly places ships on a board
def create_ships(board):
    for ship in range(5):
        ship_row, ship_col = randint(0,7), randint(0,7)
        while board[ship_row][ship_col] == '*':
            ship_row, ship_col = randint(0, 7), randint(0, 7)
        board[ship_row][ship_col] = '*'


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == '*':
                count += 1
    return count

def start game()

start game()
# Defines what board the ships should be placed on
create_ships(Hidden_Pattern)

#print(create_board(Hidden_Pattern))


# Text to start the game
print("\nWELCOME TO BATTLESHIP")
print("\nAn enemy fleet is spotted on the horizon.")
print("You have 15 missiles at your disposal.")
print("Try to sink all their ships before it's too late.\n")
time.sleep(5)

# Add press button function to begin here???

turns = 15
while turns > 0:
    # Print the board
    print("\nCan you guess where on the board the 5 hidden ships are?")
    print(create_board(Guess_Pattern))

    # Enables the player make guesses.
    
    row, column = guess_ship_location()
    if Guess_Pattern[row][column] == 'o':
        print('You have already fired a shot there, try somewhere else\n')
    elif Hidden_Pattern[row][column] == '*':
        print('YAY! YOU HIT ONE SHIP!\n')
        Guess_Pattern[row][column] = '*'
        turns -= 1
    else:
        print('Sorry,You missed\n')
        Guess_Pattern[row][column] = 'o'
        turns -= 1
    if count_hit_ships(Guess_Pattern) == 5:
        print("\nCONGRATULATIONS! YOU MANAGED TO DEFEAT THE ENEMY.\n")
        break
    print('You have ' + str(turns) + ' turns remaining ')
    if turns == 0:
        print('\nGame Over\n')
        break

