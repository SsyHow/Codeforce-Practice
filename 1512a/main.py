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

for i in range(a):

    b = II()
    L = LII()
    tmp = Counter(L)
    for i in tmp:
        if tmp[i] == 1:
            print(L.index(i)+1)

