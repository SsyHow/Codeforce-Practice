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
    n, x, y, z = MII()
    print(min((n+x-1)//x * x - n, (n+y-1)//y * y - n, (n+z-1)//z * z - n))