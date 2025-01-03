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
n = II()
L = LII()
M = LII()
L = [0] + list(accumulate(L))

print(L[M[1] - 1] - L[M[0]-1])