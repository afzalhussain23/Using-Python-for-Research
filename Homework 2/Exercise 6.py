def row_win(board, player):
    for i in range(3):
        return board[i][0] == player and board[i].count(board[i][0]) == len(board[i])

row_win(board, 1)