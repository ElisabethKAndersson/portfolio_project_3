from random import randint

"""
Builds basic board layout.
"""
def build_board(size):
    return [['~'for x in range(8)] for y in range (8)]

def player_board(board):
    for b in board:
        print(*b)
  

def npc_board(board):
    for b in board:
        print(*b)

board = build_board(4)


def create_ships(npc_board):
    for ship in range(6):
        ship_r, ship_cl=randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] =='@':
            ship_r, ship_cl = randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] = '@'

def run_game():
    print("\nWELCOME TO BATTLESHIP")
    print("\nAn enemy fleet is spotted on the horizon.")
    print("Try to sink all their ships before they sink your ships.\n")



run_game()
print("Your board")
create_ships(npc_board)
player_board(board)
print("\nOpponents board")
npc_board(board)
