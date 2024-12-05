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


def checks(x, y, m, b):
    j = 0
    i = 0
    while i < y and j < x:
        # print(i, j, )

        if b[i] == m[j]:
            j += 1
        i += 1
    # print("***", j)
    return j == x


a = II()
for _ in range(a):
    x, y = MII()
    s = I()
    b = I()
    j = 0
    i = 0
    while i < y and j < x:
        # print(i, j, )

        if b[i] == s[j]:
            j += 1
        i += 1
    # print("***", j)
    print(j)


