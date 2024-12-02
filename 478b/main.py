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
a, b = MII()

maxi = comb(a - b + 1, 2)


print( a % b * comb(a//b + 1, 2) + (b - a%b) * comb(a//b , 2), maxi)