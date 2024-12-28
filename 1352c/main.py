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
    print(y // (x - 1) * x + y % (x-1)) if y % (x-1) >0 else print(y // (x - 1) * x - 1)