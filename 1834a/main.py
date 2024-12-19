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
    b = II()
    L = LII()

    c = Counter(L)
    ans = 0
    # print(c)
    if c.get(-1, 0) >= b // 2:
        ans = max(c.get(-1, 0) -  b // 2, 0)
    if (c.get(-1, 0) - ans) % 2 == 1:
        ans += 1
    print(ans)