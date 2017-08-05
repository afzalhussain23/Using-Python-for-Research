def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if(row_win(board, player) or col_win(board, player) or diag_win(board, player)):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

evaluate(board)