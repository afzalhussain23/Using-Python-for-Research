def col_win(board, player):
    for i in range(3):
        return board[0][i] == player and board[1:][i] == board[:-1][i]

col_win(board, 1)