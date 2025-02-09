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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = II()
for _ in range(a):
    k,b = MII()
    x1, y1 = MII()
    x = x1
    y = y1
    for _ in range(k-1):
        m, n = MII()
        x += m
        y += n

    print((x + b - x1) * 2 + (y + b - y1) * 2)
