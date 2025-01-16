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
    k, j = b & 1, c & 1

    if k == j == 0:
        print(b // 2, c // 2)
    elif k == j == 1:
        x = (b + c) // 2
        if b >= x:
            b -= x
        if c > x:
            c -= x
        print(b, c)

    else:
        print(-1, -1)