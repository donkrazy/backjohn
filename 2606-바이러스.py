n = int(input())
i = input()
# aa = []
tree = {}

for j in range(int(i)):
    ist = sorted(list(map(int, input().split(" "))))
    a, b = int(ist[0]), int(ist[1])
    if tree.get(a):
        tree[a].append(b)
    else:
        tree[a] = [b, ]
    if tree.get(b):
        tree[b].append(a)
    else:
        tree[b] = [a, ]

# print(tree)
init = 1
global result, count
result = [0] * n
count = 0


def rise(init, tree, result, count):
    for j in tree[init]:
        result[j - 1] = 1
        if count == len(tree):
            break
        if tree.get(j) is None:
            continue
        count += 1
        rise(j, tree, result, count)


def rise2(init, tree):
    for j in tree[init]:
        if result[j - 1] is 0:
            result[j - 1] = 1
            # print(result)
        elif result[j - 1] is 1:
            continue
        if tree.get(j) is None:
            continue
        rise2(j, tree)

# rise(init, tree, result, count)
# print(result)

rise2(init, tree)
print(sum(result) - 1)
