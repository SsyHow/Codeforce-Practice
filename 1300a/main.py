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
    b = II()
    L = LII()
    ans =0
    if 0 in L:
        ans += L.count(0)
    if sum(L) + L.count(0) == 0:
        ans += 1
    print(ans)
