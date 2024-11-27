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

a = II()
for _ in range(a):
    c = Counter(I())
    s = ''

    for i in c:
        s += c[i] * i
    print(s)