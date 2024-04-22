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

a = I()
b = I()
c = I()

left = Counter(a) + Counter(b)
right = Counter(c)

if left == right:
    print("YES")
else:
    print("NO")
