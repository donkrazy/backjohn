# python recursion is fuck
# import sys
# sys.setrecursionlimit(5000)

# get values of first line
(m, n) = tuple(map(int, input().strip().split(" ")))

# get miro values and generate 2-dim'l void array
ans = [[0 for x in range(n)] for y in range(m)]

# set the number of candies
miro = []
for i in range(m):
    miro.append(list(map(int, input().strip().split(" "))))

# initial value and boundary value
ans[0][0] = miro[0][0]
for i in range(1, m):
    ans[i][0] = ans[i - 1][0] + miro[i][0]
for j in range(1, n):
    ans[0][j] = ans[0][j - 1] + miro[0][j]

# bottom-up
for i in range(1, m):
    for j in range(1, n):
        if ans[i - 1][j] >= ans[i][j - 1]:
            ans[i][j] = miro[i][j] + ans[i - 1][j]
        else:
            ans[i][j] = miro[i][j] + ans[i][j - 1]

# print answer
print(ans[m - 1][n - 1])
