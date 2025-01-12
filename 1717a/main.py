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
from math import lcm, gcd
a = II()
for _ in range(a):
    b = II()
    cnt = b + b // 2 * 2 + b // 3 * 2
    print(cnt)