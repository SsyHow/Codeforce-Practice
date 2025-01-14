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
    b = II()
    x = y = 0
    for _ in range(b):
        m, n = MII()
        x = max(m, x)
        y = max(n, y)

    print((x+y) * 2)