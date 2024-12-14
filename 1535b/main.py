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

from math import gcd
a = II()
for _ in range(a):
    b = II()
    cnt = 0
    M = []
    L = LII()
    for i in L:
        if i % 2 == 0:
            cnt += b-1
            b -= 1
        else:
            M.append(i)

    for x in range(len(M)):
        for y in range(x+1, len(M)):
            if gcd(M[x], M[y]) > 1:
                cnt += 1
    print(cnt)