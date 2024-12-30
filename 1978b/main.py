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
    n, x, y = MII()
    if x >= y :
        print(x * n)
    else:

        m = min(n, y - x)
        print((y + max(x+1, y-m+1)) * m //  2 + (n-m) * x)