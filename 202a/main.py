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
from collections import Counter
s = list(I())
s.sort()
c = Counter(s)

print(s[-1] * c[s[-1]])

