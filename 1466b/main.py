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
    b = II()
    L = LII()

    s = set()
    for i in L:
        # print(i)
        v = i
        if i in s:
            v += 1
        s.add(v)
        # print(s)
    print(len(s))

