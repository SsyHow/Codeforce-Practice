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
    m, n = L.index(min(L)) + 1, len(L) - L.index(min(L))
    m1, n1 = L.index(max(L)) + 1, len(L) - L.index(max(L))
    # print(m, n, m1, n1)
    print(min(max(m, m1), max(n, n1), m+n1, n+m1))