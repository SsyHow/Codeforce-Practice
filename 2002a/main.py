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
    if x >= z and y >= z:
        print(z * z)
    elif z >= x and z >= y:
        print(x * y)
    else: print(min(x, y)* z)