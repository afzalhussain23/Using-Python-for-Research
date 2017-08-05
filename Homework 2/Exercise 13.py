import time
winner = []
start = time.time()
for i in range(1000):
    winner.append(play_strategic_game())
end = time.time()
print(start - end)
plt.hist(winner)
plt.show()