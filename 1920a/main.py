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
    l, r = 0, float('inf')
    L = set()
    for _ in range(b):
        c, k = MII()
        if c == 1:
            l = max(l, k)
        elif c == 2:
            r = min(r, k)
        else:
            L.add(k)

    ans = max(0, r - l+1)
    for i in L:
        if l <= i <= r:
            ans -= 1
    print(ans)
