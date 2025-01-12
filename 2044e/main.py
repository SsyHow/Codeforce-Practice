
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
from math import log
a = II()
for _ in range(a):
    k, l1, r1, l2, r2 = MII()
    cnt = 0
    for i in range(32):
        # print(r1, (r2+(k ** i)-1)//(k ** i))
        # print(l1, (r1 + (k ** i) - 1)// (k**i))
        # print(max(min(r1, (r2 //(k ** i))) - max(l1, (l2 + (k ** i) - 1)//(k**i)) +1, 0))
        cnt += max(min(r1, (r2 //(k ** i))) - max(l1, (l2 + (k ** i) - 1)//(k**i)) + 1, 0)
    print(cnt)
