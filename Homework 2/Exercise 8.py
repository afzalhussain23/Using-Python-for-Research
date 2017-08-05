def diag_win(board, player):
    return board[0][0] == board[1][1] == board[2][2] == player
    
diag_win(board, 1)