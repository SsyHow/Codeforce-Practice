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

from collections import defaultdict
a = II()
for _ in range(a):
    i = I()
    b = defaultdict(int)
    for j in i:
        b[j] += 1
        if b[j] == 3:
            print(j)
            break
    b = {}
