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
from math import comb
a = I()
b = I()

q = pos = 0

for i in a:
    if i == '+':
        pos += 1
    else:
        pos -= 1

for i in b:
    if i == '+':
        pos -= 1
    elif i == '?':
        q += 1

    else:
        pos += 1

pos = abs(pos)

if pos <= q:

    pos = (q - pos) // 2

    # print(comb(q, pos), q, pos)
    print((comb(q, pos))/(2 ** q))
else:
    print(0)