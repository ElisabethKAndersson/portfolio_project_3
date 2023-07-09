from random import randint

class Battleship: 
    
    #Global variables for starting up game.
    
    def __init__(self): 
        self.user_board = []
        self.computer_board = []
        self.user_hits = 0
        self.computer_hits = 0
        self.ships = 5
          

    def start(self):

        #Function to create both boards and place ships.

        self.user_board = self.create_boards()
        self.computer_board = self.create_boards()
        self.display_boards()
        self.user_board  = self.place_ships(self.user_board)
        self.computer_board = self.place_ships(self.computer_board)
        #self.guess_place = []


    def create_boards(self):

        # Board layout to be used in both
                
        num = 8

        ls = [['~'for x in range(num)] for y in range (num)]
        some_str = ''
        for i in range (len(ls)):
            some_str+=" ".join(ls[i])+'\n'
        return(some_str)

    
    def place_ships(num):
        
            """
        This function generates a random placement of ships on a battleship game board.
    
        Parameters:
        num (int): The size of the game board
    
        Returns:
        str: A string representation of the game board with ship placements
        """
        try:
            # Check if the input is a positive integer
            if not isinstance(num, int) or num <= 0:
                raise ValueError("Input must be a positive integer")
        
            # Create an empty game board
            ls = [['~' for x in range(num)] for y in range(num)]
            
            # Place random ships on the game board
            for i in range(num):
                x = random.randint(0, num-1)
                y = random.randint(0, num-1)
                ls[x][y] = 'S'
            
            # Generate a string representation of the game board
            some_str = ''
            for i in range(len(ls)):
                some_str += " ".join(ls[i]) + '\n'
            
            return some_str
        except ValueError as e:
            # Log the error
            print(f"Error: {e}")
            return ''
        
            
    """
     def guess_place(self.computer_board):
        x = input("Write a row number 0-7:\n")
        y = input("Write a column number 0-7:\n")
    
    """

    def display_boards(self):
        print("\nWELCOME TO BATTLESHIP")
        print("\nAn enemy fleet is spotted on the horizon.")
        print("Try to sink all their ships before they sink your ships.\n")
        print("Your board:")
        print(self.user_board)
        print("Computer board:")
        print(self.computer_board)

        self.place_ships(self.computer_board)
        self.place_ships(self.user_board)
        self.guess_place(self.computer_board)
        
battleship = Battleship()
# start the game
battleship.start()