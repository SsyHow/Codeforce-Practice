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

from math import gcd
a, b, n = MII()
flag = True
while n > 0:
    if flag:
        n -= gcd(a, n)

    else:
        n -= gcd(b, n)
    flag = not flag

print(0) if not flag else print(1)