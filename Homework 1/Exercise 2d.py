import numpy as np

x = np.array([0, 0])
y = np.array([1, 1])

def in_circle(x, origin=[0]*2):
    return distance(x, origin) < 1

print(in_circle(y, x))