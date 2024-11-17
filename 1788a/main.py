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

from math import prod
a = II()
for _ in range(a):
    b = II()
    c = LII()
    l = 1
    r = prod(c)
    for i in range(b):
        l *= c[i]
        r //= c[i]
        # print(l,r)
        if l == r:
            print(i+1)
            break
    else:
        print(-1)