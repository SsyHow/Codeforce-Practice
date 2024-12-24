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
    x, y = MII()
    L = LII()

    while y > 0:
        l = 0
        while L[l] == 0 and l < x - 1:
            l += 1
        if l == x - 1:
            break
        aa = min(L[l], y)
        L[l] -= aa
        L[-1] += aa
        y -= aa
    print(*L, sep = ' ')