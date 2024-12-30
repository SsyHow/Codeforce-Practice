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
    ans = 0
    x, y = MII()
    c = Counter(LII())
    for i in c:
        ans += min(c[i], y)

    print(ans)
