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
    x, y, m, n = MII()
    if (y - x) % (m + n) == 0:
        print((y - x) // (m + n))
    else:
        print(-1)