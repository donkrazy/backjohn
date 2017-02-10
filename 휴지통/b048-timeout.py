# python recursion is fuck
import sys
sys.setrecursionlimit(5000)

# get values of first line
(n, m) = tuple(map(int, input().strip().split(" ")))

# get miro values and generate 2-dim'l void array
ans = [[0 for x in range(m)] for y in range(n)]
miro = []
for i in range(n):
    miro.append(list(map(int, input().strip().split(" "))))


# recursive function
def go(a, b):
    # memoization
    if ans[a][b] is not 0:
        return ans[a][b]

    # initialize
    if a == b == 0:
        ans[a][b] = miro[a][b]
        return ans[a][b]

    # boundary control
    if a == 0:
        ans[a][b] = go(a, b - 1) + miro[a][b]
        return ans[a][b]
    if b == 0:
        ans[a][b] = go(a - 1, b) + miro[a][b]
        return ans[a][b]

    # compare left and upper value
    if go(a - 1, b) >= go(a, b - 1):
        ans[a][b] = go(a - 1, b) + miro[a][b]
        return ans[a][b]

    if go(a - 1, b) < go(a, b - 1):
        ans[a][b] = go(a, b - 1) + miro[a][b]
        return ans[a][b]

# print an answer
print(go(n - 1, m - 1))
