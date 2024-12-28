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
    L = [0] * y
    for i in range(y):
        m, n = MII()
        L[m-1] += n
    L.sort(reverse=True)
    print(sum(L[:x]))