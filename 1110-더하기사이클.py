def cal1(input):
    b = input % 10
    a = (input - b) / 10
    if(input < 10):
        b = input
        a = 0
    c = (a + b) % 10
    return c


def cal2(input):
    i = input % 10
    j = cal1(input)
    return int(10 * i + j)


def main():
    i = int(input())
    n = 0
    tem = i

    while(True):
        i = cal2(i)
        n = n + 1
        if(tem == i):
            break
    print(n)

if __name__ == '__main__':
    main()
