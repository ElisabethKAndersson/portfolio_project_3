def build_board(size):
    return [['~'] * 8 for x in range(8)]


def print_board(board):
    for b in board:
        print(*b)
board = build_board(4)
print_board(board)