import random

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
        self.user_board  = self.place_ships()
        self.computer_board = self.place_ships()

        #self.guess_place = []


    def create_boards(self):

        # Board layout to be used in both
                
        num = 8

        board = [['~'for x in range(num)] for y in range (num)]
        some_str = ''
        for i in range (len(board)):
            some_str+=" ".join(board[i])+'\n'
        return(some_str)

    
    def place_ships(self):
        for ships in range(6):
            num_ships = 0
            while num_ships < ships:
                x = random.randint(0, 7)
                y = random.randint(0, 7)
                if self.board[x][y] == '~':
                    self.board[x][y] = '@'
                    num_ships += 1
                
        
   
    def guess_place(self, board):
        int(input("Write a row number 0-7:\n"))
        int(input("Write a column number 0-7:\n"))
        if board[x][y] == '@':
            print("Hit!")
            self.user_hits += 1
        else:
            print("Miss!")
        
    

    def display_boards(self):
        print("\nWELCOME TO BATTLESHIP")
        print("\nAn enemy fleet is spotted on the horizon.")
        print("Try to sink all their ships before they sink your ships.\n")
        print("Your board:")
        print(self.user_board)
        print("Computer board:")
        print(self.computer_board)
        print(self.guess_place)


        """
        self.place_ships(self.computer_board)
        self.place_ships(self.user_board)
        self.guess_place(self.computer_board)
        """

battleship = Battleship()
# start the game
battleship.start()