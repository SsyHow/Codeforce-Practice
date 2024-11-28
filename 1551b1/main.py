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
    c = I()
    even, odd = 0,0
    for i in set(list(c)):
        if c.count(i) > 1:
            even += 1
        else:
            odd += 1
    print(even + odd // 2)