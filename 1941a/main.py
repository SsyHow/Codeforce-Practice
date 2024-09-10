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
for i in range(a):
    n, m, k = MII()
    L = LII()
    M = LII()
    cnt = 0
    for i in range(n):
        for j in range(m):
            if L[i] + M[j] <= k:
                cnt += 1
    print(cnt)