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
c = Counter(LI())
# print(c)
print(c['4'] + c['3'] + (c['2']*2 + max(0, c['1'] - c['3']) + 3) // 4)