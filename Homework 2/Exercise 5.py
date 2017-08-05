board = create_board()
for i in range(3):
    for player in [1, 2]:
        random_place(board, player)

print(board)