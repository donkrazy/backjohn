# 기본 unit
class Node:

    def __init__(self, value):
        self.value = value
        self.max_value = 0
        self.left = 0
        self.right = 9
        self.temp = -1

    def set_max(self, value):
        self.max_value = value

# 입력 받아서 tree 생성. tree는 Node 객체의 2차원 배열
tree = []
n = int(input())
for i in range(n):
    temp = input().strip().split(" ")  # 입력값에 공백 있을 시 런타임에러
    temp = list(map(int, temp))
    temp = list(map(Node, temp))
    tree.append(temp)

# 점화식(?) 초기값
init_value = tree[0][0]
init_value.max_value = init_value.value
init_value.temp = init_value.value

# n=k층까지 계산된 상태에서 n = k+1층을 계산
for i in range(len(tree) - 1):
    for j in range(len(tree[i])):
        if tree[i + 1][j].temp is -1:
            tree[i + 1][j].temp = tree[i][j].max_value
        elif tree[i + 1][j].temp <= tree[i][j].max_value:
            tree[i + 1][j].temp = tree[i][j].max_value
        else:
            pass

        if tree[i + 1][j + 1].temp is -1:
            tree[i + 1][j + 1].temp = tree[i][j].max_value
        elif tree[i + 1][j + 1].temp <= tree[i][j].max_value:
            tree[i + 1][j + 1].temp = tree[i][j].max_value
        else:
            pass

    for j in range(len(tree[i]) + 1):
        tree[i + 1][j].set_max(tree[i + 1][j].temp + tree[i + 1][j].value)

# 시험용 출력
'''
for item in tree:
    for i in item:
        print(i.max_value, end=", ")
    print("")
'''

# tree 마지막 층의 최댓값 출력
result = []
for item in tree[len(tree) - 1]:
    result.append(item.max_value)
print(sorted(result).pop())
