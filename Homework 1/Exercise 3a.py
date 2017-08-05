def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    ans = []
    for i in range(n):
        ans.append(sum(x[i:i+width])/width)
    return ans

x=[0,10,5,3,1,5]
print(moving_window_average(x, 1))