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

from itertools import accumulate

a = II()
L = LII()
L = [0] + list(accumulate(L))
b = II()
M = LII()
for i in M:
    l, r = 0, a-1
    while l <= r:
        mid = (l + r) // 2
        if L[mid] >= i:
            r = mid - 1
        else:
            l = mid + 1
    print(l)
