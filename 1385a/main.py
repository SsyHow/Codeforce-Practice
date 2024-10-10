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
    x, y, z = sorted([x, y, z])
    if y != z:
        print("NO")
        continue
    else:
        print("YES")
        print(x,x,y)