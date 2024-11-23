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

from math import sqrt
a = II()
L = [1] * 10 ** 6
vis = set()
for i in range(2, 10 **6):
    if L[i]:
        vis.add(i*i)
    for k in range(2*i, 10 **6, i):
        L[k] = 0

# print(L[])
for i in MII():
    print("YNEOS"[not(i in vis)::2] )