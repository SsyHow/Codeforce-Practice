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

for _ in range(II()):
    n, a, b, c = MII()

    x = n // (a + b +c)
    i = 0
    n -= x * (a+b+c)
    if n > 0:
        i += 1
        n -= a
    if n > 0:
        i += 1
        n -= b
    if n > 0:
        n -= c
        i += 1

    print(i + x * 3)
