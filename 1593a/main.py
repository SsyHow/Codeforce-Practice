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
    maxi = max(x, y, z)
    m = 0 if x > y and x > z else maxi - x + 1
    n = 0 if y > z and y > x else maxi - y + 1
    q = 0 if z > y and z > x else maxi - z + 1
    print(m ,n, q)
