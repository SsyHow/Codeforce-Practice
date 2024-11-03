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
    c = sum(L)
    if c % 3 == 0:
        print(0)
    elif c % 3 == 2 or any(c % 3 == i % 3 for i in L):
        print(1)
    else:
        print(2)



