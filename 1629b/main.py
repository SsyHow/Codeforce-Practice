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
    x, y, z = MII()

    if (y - x + 1) - (y//2 - (x - 1) // 2) <= z:
        print("YES")
    elif x == y and x != 1:
        print("YES")
    else:
        print("NO")