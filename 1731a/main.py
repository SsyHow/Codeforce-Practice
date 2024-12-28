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
from math import prod
a = II()
for _ in range(a):
    b = II()
    L = LII()
    print((prod(L) + (b-1)) * 2022)
