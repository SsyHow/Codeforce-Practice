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
        L = LII()
        print(-1)
        continue
    for _ in range(x):
        L = LII()
        print(*[(i+0) % (x*y) + 1 for i in L])

