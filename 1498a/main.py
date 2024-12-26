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

    while gcd(b, sum(list(map(int, list(str(b)))))) == 1:

        b += 1
    print(b)