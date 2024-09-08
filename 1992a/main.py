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

    for _ in range(5):
        x, y, z = sorted((x, y, z))
        x += 1

    print(x * y * z)

