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
    L = LII()
    minx = min(L)
    maxx = max(L)
    ans = 100
    for i in range(minx, maxx + 1):
        ans = min(ans, sum([abs(x - i) for x in L]))
    print(ans)