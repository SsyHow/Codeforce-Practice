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
from collections import  Counter
a = II()
for _ in range(a):
    b, c = MII()
    x = Counter(LII())
    ans = b
    for i in x:
        if x[i] >= c:
            ans = c - 1
            break
    print(ans)
