# import sys
# sys.setrecursionlimit(15000)

input_number = int(input("input variable"))


i = 0
dd = [None] * (input_number + 1)

while True:
    i += 1
    b = i * i
    if b > input_number:
        break
    dd[b] = 1

for j in range(1, i + 1):
    for k in range(1, j + 1):
        z = j * j + k * k
        if z > input_number:
            continue
        if dd[z] is None:
            dd[z] = 2


def go(a):
    x = 100
    i = 1
    y = 0
    if dd[a] is not None:
        return dd[a]

    while i * i < a:
        y = go(a - i * i) + 1
        if y < x:
            x = y
        i += 1

    dd[a] = x
    return dd[a]

print(go(input_number))
