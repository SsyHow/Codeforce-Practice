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
    b = Counter(I())
    if b['A'] + b['C'] == b['B']:
        print('YES')
    else:
        print("NO")

