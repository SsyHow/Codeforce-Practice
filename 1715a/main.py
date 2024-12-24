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
    if x == y == 1:
        print(0)
    else:
        l1 = y - 1 + x - 1
        l2 = min(x, y)

        print(l1 + l2)