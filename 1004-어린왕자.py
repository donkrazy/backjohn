import math


def is_included(x, y, circle_info):
    # check if point (x, y) is located in circle_info
    cx, cy, r = circle_info
    d = math.sqrt((x - cx) * (x - cx) + (y - cy) * (y - cy))
    return d < r

n = int(input())
for i in range(0, n):
    x1, y1, x2, y2 = (int(j) for j in input().split())
    k = int(input())
    count = 0

    for l in range(0, k):
        circle_info = [int(m) for m in input().split()]
        # count 'XOR' only
        if is_included(x1, y1, circle_info) != is_included(x2, y2, circle_info):
            count = count + 1

    print(count)
