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

import re

a = II()
for _ in range(a):
    b = II()
    c = I()

    print(c.count('map') + c.count('pie') - c.count('mapie'))
