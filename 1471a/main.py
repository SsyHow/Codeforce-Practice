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

    m = (sum(L) + c - 1) // c
    n = sum([(i + c - 1)//c for i in L])
    print(m,n)