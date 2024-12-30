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
    if (c := abs(x - y)) <= 1:
        print(x + y)
    else:
        print(c * 2 - 1 + min(x, y) * 2)