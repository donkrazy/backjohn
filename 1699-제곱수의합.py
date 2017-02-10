# 입력 받음
input_number = int(input())

# 결과 배열 초기화
result_set = [None] * (input_number + 1)


# 함수 정의
def search(p):
    if result_set[p] is not None:
        return result_set[p]
    q = 1
    minimum = 10
    while q * q < p:
        if result_set[p - q * q] is not None and result_set[p - q * q] < minimum:
            minimum = result_set[p - q * q]
        q += 1
        if minimum is 1:
            break
    return minimum + 1


def go(input_num):
    for x in range(1, input_num + 1):
        result_set[x] = search(x)


# 제곱수 결과를 배열에 넣는다(정답이 1인 것들)
i = 0
while True:
    i += 1
    b = i * i
    if b > input_number:
        break
    result_set[b] = 1

# 제곱수의 합 결과를 배열에 넣는다(정답이 2인 것들)
for j in range(1, i + 1):
    for k in range(1, j + 1):
        z = j * j + k * k
        if z > input_number:
            continue
        if result_set[z] is None:
            result_set[z] = 2

# 정답이 1이나 2인 것은 먼저 프린트
if result_set[input_number] is not None:
    print(result_set[input_number])
# 정답이 3이상인 것은 iteration 이용하여 계산(위의 함수 이용)
else:
    go(input_number)
    print(result_set[input_number])
