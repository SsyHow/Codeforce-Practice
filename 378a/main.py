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

a, b = MII()
x = y = z = 0
for i in range(1, 7):
    if abs(a - i) < abs(b - i):
        x += 1
    elif abs(a - i) == abs(b - i):
        y += 1
    else:
        z += 1
print(x, y, z)