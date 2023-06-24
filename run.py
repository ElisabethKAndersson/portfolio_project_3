
def build_board(size):
    return [['~'] * 8 for x in range(8)]


def player_board(board):
    for b in board:
        print(*b)

def npc_board(board):
    for b in board:
        print(*b)

board = build_board(4)
print("Your board")
player_board(board)
print("\nOpponents board")
npc_board(board)



def run_game():
    print("WELCOME TO BATTLESHIP")
    print("An enemy is spotted on the horizon")
    print("Try to sink all their ships before they sink your ships")
    
run_game()