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

from math import ceil
a = II()
for _ in range(a):
    b = II()
    L = LII()

    mean = ceil(sum(L) / len(L))
    print(mean)
