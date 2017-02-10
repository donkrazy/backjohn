# generate Fibonacci set and result set
global a
a = [1, 1]

last = 1
while last < 1000000000:
    temp = a[len(a) - 1] + a[len(a) - 2]
    a.append(temp)
    last = temp
# print(a) ㅅㅂ


# recursive function
def calculate(input, result):
    # exit condition
    if input in a:
        result.append(input)
        for i in sorted(result):
            print(i, end=" ")
        print("")
        return
    i = 0
    while input > a[i]:
        i += 1
    result.append(a[i - 1])
    input -= a[i - 1]
    calculate(input, result)


# gogo
n = int(input())
problem_set = []
for j in range(n):
    input_num = int(input())
    problem_set.append(input_num)
for item in problem_set:
    calculate(item, [])
