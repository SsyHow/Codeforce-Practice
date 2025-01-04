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
    _ = I()
    x1, y1 = MII()
    x2, y2 = MII()
    x3, y3 = MII()

    if (x1 == x2 or x2 == x3 or x1 == x3) and (y1 == y2 or y2 == y3 or y1 == y3):
        print("NO")
    else:
        print("YES")