def build_board(size):
    return [['~' for count in range(size)] for count in range(size)]
build_board(8)

def print_board(board):
    for b in board:
        print(*b)
board = build_board(4)
print_board(board)