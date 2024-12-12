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

from math import comb

a = II()
for i in range(a):
    b = II()
    s = I()
    print((comb(10 - b, 2) * 6))