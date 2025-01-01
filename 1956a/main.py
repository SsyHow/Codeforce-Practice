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
    L = LII()
    M = LII()
    for i in M:
        print(min(i, L[0] - 1), end=' ')
    print()
