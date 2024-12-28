from math import gcd
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

a = II()

for _ in range(a):
    a, b = MII()
    if gcd(a, b) == 1:
        print(1)
        print(a, b)
    else:
        print(2)
        print(1, b-1)
        print(a, b)