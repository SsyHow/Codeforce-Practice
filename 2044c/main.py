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

x = II()
for _ in range(x):
    m, a, b, c = MII()

    ans = 0
    fl = max(m - a, 0)
    ans += m if fl == 0 else a
    if fl > 0:
        ans += min(fl, c)
        c = max(c - fl, 0)

    sl = max(m-b, 0)
    ans += m if sl == 0 else b
    if sl > 0:
        ans += min(sl, c)
    print(ans)


