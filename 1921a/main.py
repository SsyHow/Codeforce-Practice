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
    x = set()
    y = set()
    for _ in range(4):
        x1, y2 = MII()
        x.add(x1)
        y.add(y2)
    x, y = list(x), list(y)
    print(abs(x[0] - x[1]) * abs(y[0] - y[1]))
