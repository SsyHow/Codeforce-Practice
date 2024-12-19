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
    x, y = MII()

    g = abs(x - y)

    if g == 0:
        print(0,0)
    else:
        print(g, min(x % g, g - x % g))