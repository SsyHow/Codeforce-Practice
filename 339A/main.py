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

a = I()
from collections import defaultdict
b = defaultdict(int)
for i in a:
    if i == '+':
        continue
    b[i] += 1

c = sorted(b.keys())

L = []
for i in c:
    L.extend([i] * b[i])
# print(L)
print('+'.join(L))
