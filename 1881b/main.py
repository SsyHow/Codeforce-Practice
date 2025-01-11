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
    x, y, z = sorted(MII())
    if y % x or z % x:
        print("NO")
    elif y // x - 1 + z // x - 1 <= 3:
        print("YES")
    else:
        print("NO")