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
    x, y, n = MII()
    r, c = (n - 1) // x + 1, (n - 1) % x + 1
    # print(r, c)
    print((c-1)*y + r)