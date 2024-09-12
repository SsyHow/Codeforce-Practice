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
    x, y, n = MII()
    x, y = sorted((x, y))
    cnt = 0
    # print(x, y)
    while x + y <= n:
        x, y = sorted((x, y))
        x += y
        cnt += 1
    print(cnt+1)