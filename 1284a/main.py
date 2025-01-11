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

a, b = MII()
L = LI()
M = LI()

c = II()
for _ in range(c):
    x = II() - 1
    print(L[x%a], M[x%b], sep='')
