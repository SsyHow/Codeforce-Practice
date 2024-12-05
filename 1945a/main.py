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
    x, y, z = MII()

    if y % 3 and y % 3 + z <= 2:
        print(-1)
    else:
        x = x
        yy = y // 3 + 1 if y % 3 else y // 3
        if y % 3 == 0:
            zz = z // 3 if z % 3 == 0 else z // 3 + 1
        else:
            zz = (z - (3 - y % 3)) // 3 if (z - (3 - y % 3)) % 3 == 0 else (z - (3 - y % 3)) // 3 + 1
        print(x + yy + zz)