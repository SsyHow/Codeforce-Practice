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
a = II()
for _ in range(a):
    n, k = MII()
    L = LII()

    L.sort()

    ans = 0
    j = 0

    for i in range(n):
        j = max(i, j)
        # print(i,j)
        while j + 1 < n and L[j + 1] - L[j] <= 1 and L[j+1] - L[i] < k:
            j += 1
        ans = max(ans, j - i + 1)
    print(ans)

