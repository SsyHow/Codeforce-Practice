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
for i in range(a):
    b = II()
    L = LII()
    c = sum(L)
    if int(sqrt((c))) == sqrt((c)):
        print("YES")
    else:
        print("NO")