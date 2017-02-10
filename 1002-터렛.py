import math
n = int(input())
for i in range(0, n):
    x1, y1, r1, x2, y2, r2 = (int(n) for n in input().split())
    d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
    # one circle
    if d == 0 and r1 == r2:
        print(-1)
    # on border
    elif d == r1 + r2 or d == math.fabs(r1 - r2):
        print(1)
    # cannot make triangle
    elif d > r1 + r2 or r1 > d + r2 or r2 > d + r1:
        print(0)
    else:
        print(2)
