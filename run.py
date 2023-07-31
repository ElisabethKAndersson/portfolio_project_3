"""
Import random module for random placement of ships.
Import time module to create delays.
"""
from random import randint
import time
import os

print("WELCOME TO BATTLESHIP\n")
name = input('What is your name?\n')
print('\nThank God you are here Captain ' + name + '!')
print("\nAn enemy fleet is spotted on the horizon.")
print("We have to sink all their ships before it's too late!\n")
input('Press enter to start')
os.system('clear')


# Function that runs the game from the beginning.
def start_game():
   
    try:
        num = int(input('Add number of rows/columns (4-8)?\n'))
        while num not in range(4, 9):
            print('That is not a valid number.')
            num = int(input('Add number of rows/columns (4-8)?\n')) 

        ships = int(input('Add number of ships to hit (3-6).\n')) 
        while ships not in range(3, 7):
            print('That is not a valid number.')
            ships = int(input('Add number of ships to hit (3-6).\n'))

        turns = int(input('Add number of turns (10-20)'))
        while turns not in range(10, 21):
            print('That is not a valid number.')
            turns = int(input('Add number of turns (10-20)'))
    except ValueError:
        print("Invalid input. Please enter a single digit.")
        return start_game()

    # Function for guessing where on the board the hidden ships are
    def guess_ship_location():
        try:
            row = int(input('Enter a row number 0-' + str(num - 1) + '/n'))
            while row not in range(num):
                print('That is not a valid row number')
                row = int(input('Enter a number 0-' + str(num - 1)))
            column = int(input('Enter a row number 0-' + str(num - 1)))
            while column not in range(num):
                print('That is not a valid column number')
                column = int(input('Enter a number 0-' + str(num - 1)))
            return int(row), int(column)
        # If something that isn't an integer is inserted from the user.
        except ValueError:
            print("Invalid input. Please enter a single digit.")
            return guess_ship_location()


    # Function that randomly places ships on a board
    def create_ships(board):
        for ship in range(ships):
            ship_row, ship_col = randint(0, int(num-1)), randint(0, int(num-1))
            while board[ship_row][ship_col] == '*':
                ship_row, ship_col = randint(0, int(num-1)), randint(0, int(num-1))
            board[ship_row][ship_col] = '*'


    def count_hit_ships(board):
        count = 0
        for row in board:
            for column in row:
                if column == '*':
                    count += 1
        return count

    # Board resets at the start of the game.
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

    # Places the ships on the hidden board
    create_ships(Hidden_Pattern)
    # print(create_board(Hidden_Pattern))

    
    # Text when starting the game.
    
    print("You have " + str(turns) + " missiles at your disposal.")
    print('Where should we aim Captain ' + name + '?')
    time.sleep(2)
    

    while turns > 0:
        # Print the board
        print('\nCan you guess where on the board the ' + str(ships) + ' hidden ships are?')
        print(create_board(Guess_Pattern))

        # Enables the player make guesses.
        row, column = guess_ship_location()
        if Guess_Pattern[row][column] == 'o':
            print('\nYou have already fired a missile there\n')
            print('Choose a different space')
            time.sleep(2)
        elif Hidden_Pattern[row][column] == '*':
            print('\nYAY! YOU HIT ONE SHIP!\n')
            Guess_Pattern[row][column] = '*'
            turns -= 1
            time.sleep(2)
        else:
            print('\nMiss!\n')
            Guess_Pattern[row][column] = 'o'
            turns -= 1
            time.sleep(2)
        if count_hit_ships(Guess_Pattern) == 4:
            print("\nCONGRATULATIONS! YOU MANAGED TO DEFEAT THE ENEMY.\n")
            break
        print('you have ' + str(count_hit_ships(Guess_Pattern)) + ' hits')
        print('You have ' + str(turns) + ' turns remaining ')
        time.sleep(2)
        if turns == 0:
            print('\nGame Over\n')
            break

    # Gives option to start the game from the beginning.
    start_over = input("\nDo you want to play again? Y / N\n")
    if start_over == 'Y':
        start_game()
    else:
        print('\nThank you for playing.\n')


start_game()