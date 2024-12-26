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
    c = set(L)
    ans = 0
    vis = set()
    for i in c:
        # print(i, ans, vis)
        if i != 0 and abs(i) not in vis:
            ans += min(L.count(i) + L.count(-i), 2)
            vis.add(abs(i))
        elif i == 0:
            ans += 1
    print(ans)