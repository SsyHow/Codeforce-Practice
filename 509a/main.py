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
cnt = comb(2 * (a-1), a-1)
print(cnt)
