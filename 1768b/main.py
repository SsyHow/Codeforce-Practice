def I():
    return input()


def II():
    return int(input())


def MII():
    return map(int, input().split())


def LI():
    return list(input().split())


def LII():
    return list(map(int, input().split()))

a = II()
for _ in range(a):
    b, c = MII()
    L = LII()

    prev = tmp = 0
    flag = False
    for i in L:
        if i == 1:
            flag = True
            prev = 1
            tmp = 1
        if flag and prev == i:
            prev += 1
            tmp += 1
    # print(tmp - 1)
    print((b - tmp + 1 + (c-1)) // c)
