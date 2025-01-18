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
    r, c, m, n = MII()

    print((r*c - ((m-1) * c + n)) + (r-m) * (c-1))