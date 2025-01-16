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
    b, c = MII()
    L = LII()

    L.sort()
    ans = 0
    p = L[0]
    for i in L[1:]:
        ans += max((c - i) // p, 0)
    print(ans)