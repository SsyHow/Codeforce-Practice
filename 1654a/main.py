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

import heapq
a = II()
for _ in range(a):
    b = II()
    L = [-x for x in MII()]

    heapq.heapify(L)
    m1, m2 = heapq.heappop(L), heapq.heappop(L)
    print(-m1 - m2)