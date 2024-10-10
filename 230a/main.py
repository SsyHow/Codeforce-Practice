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
a, b = MII()
heap = []
for i in range(b):
    c, d = MII()
    if a > c:
        a += d
    else:
        heapq.heappush(heap, (c, d))

    while heap and a > heap[0][0]:
        _, d = heapq.heappop(heap)
        a += d

if heap:
    print("NO")
else:
    print("YES")