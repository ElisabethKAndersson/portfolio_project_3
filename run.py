"""
Builds basic board layout.
"""
def build_board(size):
    return [['~'] * 8 for x in range(8)]


def player_board(board):
    for b in board:
        print(*b)

def npc_board(board):
    for b in board:
        print(*b)

board = build_board(4)




def run_game():
    print("\nWELCOME TO BATTLESHIP")
    print("\nAn enemy fleet is spotted on the horizon.")
    print("Try to sink all their ships before they sink your ships.\n")


run_game()
print("Your board")
player_board(board)
print("\nOpponents board")
npc_board(board)
print(create_ships)