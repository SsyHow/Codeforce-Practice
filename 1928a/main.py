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
    x, y = MII()
    if (x == y * 2 and y % 2 == 1) or (y == x * 2 and x % 2 == 1) or x % 2 == y % 2 == 1:
        print("NO")
    else:
        print("YES")