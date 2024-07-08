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

a = II()
for _ in range(a):
    b = II()
    L = LII()
    M = LII()
    minl = min(L)
    minm = min(M)
    ans = 0
    for i in range(b):
        ans += max(L[i] - minl, M[i] - minm)
    print(ans)