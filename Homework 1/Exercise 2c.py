import math

def distance(x, y):
   X = (x[0]-y[0])**2
   Y = (x[1]-y[1])**2
   ans = math.sqrt(X + Y)
   return ans
   
x = (0, 0)
y = (1, 1)

print(distance(x, y))