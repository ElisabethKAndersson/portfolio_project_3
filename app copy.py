from random import randint

class Battleship:
    # this function runs when you create a new game
    # set up all your "global" varaibles here
    def __init__(self): 
        self.user_board = []
        self.computer_board = []
        self.user_hits = 0
        self.computer_hits = 0

    # do everything that needs to run when you start the game
    def start(self):
        # create boards
        self.user_board = self.create_boards()
        self.computer_board = self.create_boards()
        # place ships into the boards
        # pass the board into the function, when its returned reassign it
        self.user_board  = self.place_ships(self.user_board)
        self.computer_board = self.place_ships(self.computer_board)
        # display the boards
        self.display_boards()

    def create_boards(self):
        ls = [['~'for x in range(8)] for y in range (8)]
        
        some_str = ''
        for i in range (len(ls)):
            some_str+=" ".join(ls[i])+'\n'
        print(some_str)
                 

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
        print(self.user_board)
        print(self.computer_board)

    def place_ships(self, board):
        for ship in range(6):
            ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='@':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = '@'

        return board
        

# create a new class instance
battleship = Battleship()
# start the game
battleship.start()