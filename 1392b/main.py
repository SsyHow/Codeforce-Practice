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


    tmp = max(L)
    for i in range(b):
        L[i] = tmp - L[i]
    L1 = L.copy()
    tmp = max(L)
    for i in range(b):
        L[i] = tmp - L[i]
    L2 = L.copy()

    print(*L1) if c % 2 == 1 else print(*L2)
