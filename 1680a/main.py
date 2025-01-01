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

    if max(x, m) <= min(y, n):
        print(max(x, m))
    else:
        print(x+m)