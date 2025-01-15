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
import bisect

a = II()
for _ in range(a):
    n ,x ,y = MII()
    L = LII()
    L.sort()
    s = sum(L)
    upp, low = s - x, s - y

    ans = 0
    for i in range(n):
        left = low - L[i]
        right = upp - L[i]
        l = bisect.bisect_left(L, left, i + 1, n)
        r = bisect.bisect_right(L, right, i + 1, n)

        ans += r - l
    print(ans)