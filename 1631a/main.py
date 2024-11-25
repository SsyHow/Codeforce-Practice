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
    M = LII()
    h, l  = float('-inf'), float("-inf")
    for i in range(b):
        x, y = max(L[i], M[i]), min(L[i], M[i])
        h = max(h, x)
        l = max(l, y)
    print(h * l)
