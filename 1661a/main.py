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
    ans = 0
    for i in range(b-1):
        ans += min(abs(L[i+1] - L[i])  + abs(M[i+1] - M[i]), abs(L[i+1] - M[i])  + abs(M[i+1] - L[i]))
    print(ans)