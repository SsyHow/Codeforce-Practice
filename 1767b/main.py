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

    x = L[0]
    L = sorted(L[1:])
    for y in L:
        if y > x:
            x += (y - x + 1) // 2
    print(x)