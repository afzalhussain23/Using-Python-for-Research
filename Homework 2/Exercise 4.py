import random
def random_place(board, player):
    selection = possibilities(board)
    idx = random.choice(selection)
    board[idx] = player
random_place(board, 2)