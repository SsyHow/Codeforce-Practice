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

aa = II()
a, b, c = 0, 0, 0
for i in range(aa):
    x, y, z = MII()
    a += x
    b += y
    c += z
if (a == 0 and b == 0 and c == 0):
    print("YES")
else:
    print("NO")