R = 1000
x = [random.uniform(0, 1) for i in range(1000)]
Y = [x] + [moving_window_average(x, n_neighbors) for n_neighbors in range(1, 10)]