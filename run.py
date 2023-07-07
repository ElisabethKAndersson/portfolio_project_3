from random import randint

class Battleship: 
    
    #Global variables for starting up game.
    
    def __init__(self): 
        self.user_board = []
        self.computer_board = []
        self.user_hits = 0
        self.computer_hits = 0


    def start(self):

        #Function to create both boards and place ships.

        self.user_board = self.create_boards()
        self.computer_board = self.create_boards()
        self.display_boards()

        self.user_board  = self.place_ships(self.user_board)
        self.computer_board = self.place_ships(self.computer_board)


    def create_boards(self):

        # Board layout to be used in both

        ls = [['~'for x in range(8)] for y in range (8)]
        some_str = ''
        for i in range (len(ls)):
            some_str+=" ".join(ls[i])+'\n'
        return(some_str)

    def place_ships(self, board):
        for ship in range(6):
            ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='@':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = '@'

        return board
    
    def display_boards(self):
        print("\nWELCOME TO BATTLESHIP")
        print("\nAn enemy fleet is spotted on the horizon.")
        print("Try to sink all their ships before they sink your ships.\n")
        print("Your board:")
        print(self.user_board)
        print("Computer board:")
        print(self.computer_board)


battleship = Battleship()
# start the game
battleship.start()