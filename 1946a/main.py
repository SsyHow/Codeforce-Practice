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
    L = sorted(LII())

    p = (b + 1) // 2 - 1
    print(L[p:].count(L[p]))
