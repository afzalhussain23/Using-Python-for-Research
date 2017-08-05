def play_game():
    board, winner = create_board(), 0
    while winner == 0:
        for player in [1, 2]:
            random_place(board, player)
            evaluate(board)
            if winner != 0:
                break
            return winner

play_game()