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
a = II()
for _ in range(a):
    b = II()
    n = gcd(100, b)
    if n ==  1:
        print(100)
    else: print(100 // n)