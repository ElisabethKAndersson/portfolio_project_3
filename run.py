"""
Import random module for random placement of ships.
Import time module to create delays.
Import os to be able to clear the board
"""
from random import randint
import time
import os

# Welcome text that only appears first playthrough.
print("WELCOME TO BATTLESHIP\n")


# Function for the player to enter their name.
def name_input():
    captain = input('What is your name?\n')
    # Message if the player presses enter without typing anything.
    if captain == "":
        print("Please enter your name.")
        return name_input()
    return captain


name = name_input()

# Welcome text at the start of the game.
print('\nThank God you are here Captain ' + name + '!')
print("\nAn enemy fleet is spotted on the horizon.")
print("We have to sink all their ships before it's too late!\n")
input('Press enter to start')


# Function that runs the game from the beginning.
def start_game():
    # Clears the board when starting.
    os.system('clear')

    # Function that lets the player decide number of rows/columns.
    def num_input():
        try:
            nums = int(input('Add number of rows/columns (5-8).\n'))
            # Validation that the player writes an integer in the right range.
            if nums not in range(5, 9):
                print("Please enter a digit between 5-8.\n")
                return num_input()
        except ValueError:
            print("Please enter a single digit.\n")
            return num_input()
        return nums

    num = num_input()

    # Function that lets the player decide number of ships.
    def ships_input():
        try:
            ship = int(input('Add number of ships to hit (3-6).\n'))
            # Check if the player typed the right value.
            if ship not in range(3, 7):
                print("Please enter a digit between 3-6.\n")
                return ships_input()
        except ValueError:
            print("Please enter a single digit.\n")
            return ships_input()
        return ship

    ships = ships_input()

    # Function that lets the player decide number of turns / missiles.
    def turns_input():
        try:
            turn = int(input('Add number of turns (10-20).\n'))
            # Check if the player typed the right value.
            if turn not in range(10, 21):
                print("Please enter a digit between 10-20.\n")
                return turns_input()
        except ValueError:
            print("Please enter number of turns in digits.\n")
            return turns_input()
        return turn

    turns = turns_input()

    os.system('clear')

    # Function for guessing where on the board the hidden ships are
    def guess_ship_location():
        print('Please enter a row number and a column number. \n')
        try:
            # Guess row number, adapts to num of players choice.
            row = int(input('Row number 0-' + str(num - 1) + ':\n'))
            while row not in range(num):
                print('That is not a valid row number\n')
                row = int(input('Row number 0-' + str(num - 1) + ':\n'))
            # Guess column number, adapts to num of players choice.
            column = int(input('Column number 0-' + str(num - 1) + ':\n'))
            while column not in range(num):
                print('That is not a valid column number\n')
                column = int(input('Column number 0-' + str(num - 1) + ':\n'))
            return int(row), int(column)
        # If something that isn't an integer is inserted from the user.
        except ValueError:
            print("Please enter a single digit.\n")
            return guess_ship_location()

    """
    Function that randomly places ships on a board.
    Adapts to num of players choice.
    """
    def create_ships(board):
        for ship in range(ships):
            ship_row, ship_col = randint(0, int(num-1)), randint(0, int(num-1))
            while board[ship_row][ship_col] == '*':
                ship_row = randint(0, int(num-1))
                ship_col = randint(0, int(num-1))
            board[ship_row][ship_col] = '*'

    # Counts number of hits.
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
    # Guess board that shows guesses.
    Guess_Pattern = [['~'for x in range(num)] for y in range(num)]

    # Creates a board grid layout with spaces in between.
    def create_board(board):
        space = ''
        for i in range(len(board)):
            space += " ".join(board[i])+'\n'
        return (space)

    # Places the ships on the hidden board
    create_ships(Hidden_Pattern)
    # Text when starting the game.
    print("You have " + str(turns) + " missiles at your disposal.")
    print('Where should we aim our next missile, Captain ' + name + '?\n')
    time.sleep(1)
    while turns > 0:
        print('\nCan you guess where on the board')
        print('the ' + str(ships) + ' hidden ships are?\n')
        # Prints the visable board that shows guesses.
        print(create_board(Guess_Pattern))

        # Enables the player make guesses.
        row, column = guess_ship_location()
        if Guess_Pattern[row][column] == 'o':
            print('\nYou have already fired a missile there.')
            print('Choose a different space\n')
            time.sleep(1)
        # Checks Hidden pattern for ships (*).
        # Prints message and adds * to Guess pattern if it is a hit.
        elif Hidden_Pattern[row][column] == '*':
            print('\nYAY! YOU HIT ONE SHIP!\n')
            Guess_Pattern[row][column] = '*'
            turns -= 1
            time.sleep(2)
        # Prints miss message and adds o to guess pattern
        else:
            print('\nMiss!\n')
            Guess_Pattern[row][column] = 'o'
            turns -= 1
            time.sleep(2)
        # If all ships are hit, message and end game.
        if count_hit_ships(Guess_Pattern) == ships:
            print("\nCONGRATULATIONS! YOU MANAGED TO DEFEAT THE ENEMY.\n")
            break
        # Informs the player of number of turns left and hits made.
        print('you have ' + str(count_hit_ships(Guess_Pattern)) + ' hits')
        print('You have ' + str(turns) + ' turns remaining\n')
        time.sleep(1)
        if turns == 0:
            print('\nGame Over\n')
            break

    # Gives option to start the game from the beginning.
    def start_over_input():
        start_over = input("\nDo you want to play again? Y / N\n")
        if start_over == 'Y':
            start_game()
        elif start_over == 'N':
            print('\nThank you for playing.\n')
        else:
            print('Write Y to play again, N to quit.')
            return start_over_input()

    start_over_input()


start_game()
