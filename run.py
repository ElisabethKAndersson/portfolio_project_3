from random import randint

class Battleship: 
"""
Global variables for starting up game
"""
    def __init__(self): 
        self.user_board = []
        self.computer_board = []
        self.user_hits = 0
        self.computer_hits = 0

    def create_boards(self):
        ls = [['~'for x in range(8)] for y in range (8)]
        
        some_str = ''
        for i in range (len(ls)):
            some_str+=" ".join(ls[i])+'\n'
        print(some_str)