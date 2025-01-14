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
    x,y,z = MII()
    if y > x or y > z + 1:
        print(-1)
    else:
        mm = z if y!= z else z -1
        print((y-1)*y//2 + (x - y) * mm)