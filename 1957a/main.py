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
    I = II()
    L = LII()
    c = Counter(L)
    ans = 0
    for i in c:
        ans += c[i] // 3
    print(ans)
