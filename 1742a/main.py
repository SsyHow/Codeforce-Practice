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
    x,y,z = MII()
    x,y,z = max(x,y,z), min(x,y,z), x+y+z - max(x,y,z) - min(x,y,z)
    if x == y + z:
        print('YES')
    else:
        print('NO')