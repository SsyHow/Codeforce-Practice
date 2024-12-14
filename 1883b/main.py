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
    b, k = MII()
    c = Counter(I())

    cnt = 0
    for i in c:
        if c[i] % 2 == 1:
            cnt += 1
    if cnt <= k + 1:
        print("YES")
    else:
        print("NO")