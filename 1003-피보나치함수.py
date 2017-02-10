n = int(input())
for i in range(0, n):
    result_set = [(1, 0), (0, 1)]
    k = int(input())

    # if index 0 or 1
    if k < len(result_set):
        print('%d %d' % (result_set[k][0], result_set[k][1]))
        continue

    for j in range(2, k + 1):
        x = (result_set[j - 1][0] + result_set[j - 2][0])
        y = (result_set[j - 1][1] + result_set[j - 2][1])
        result_set.append((x, y))

    print('%d %d' % (result_set[k][0], result_set[k][1]))
