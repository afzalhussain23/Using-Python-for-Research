R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    inside.append(in_circle(point, origin=[0]*2))

cnt = 0
for i in inside:
    if i:
        cnt = cnt + 1

print(cnt/R)