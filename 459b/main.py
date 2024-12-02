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
L = LII()
h, l = max(L), min(L)

print(h-l, L.count(h) * L.count((l))) if h != l else print(0, comb(a,2))