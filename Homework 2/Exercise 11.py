import time
winner = []
def play_game():
    board = create_board()
    for i in range(5):
        for player in [1, 2]:
            random_place(board, player)
            winner.append(evaluate(board))
            if(evaluate(board) == 1 or 2 or -1):
                break
            
start = time.time()        
for i in range(1000):
    play_game()
end = time.time()
print(start - end)
plt.hist(winner)
plt.show()