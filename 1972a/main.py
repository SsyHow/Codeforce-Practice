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
    r = l = 0

    L = LII()
    M = LII()
    ans = 0
    while r < b and l < b:
        while r < b and L[l] > M[r]:
            ans += 1
            r += 1
        l += 1
        r += 1
    print(ans )


