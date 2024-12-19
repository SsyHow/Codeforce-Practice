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

m = II()
for _ in range(m):
    b = II()
    a = LII()

    a.sort()

    print(max(a[0] * a[1], a[-1] * a[-2]))