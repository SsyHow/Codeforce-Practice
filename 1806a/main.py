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
    x, y, m ,n = MII()
    a = n - y + (n - y) - (m-x)
    if n >= y and x - m >= y - n:
        print(a)
    else:
        print(-1)