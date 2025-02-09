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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a, b = MII()
minx = maxx = -1
for i in range(a):
    s = list(I())

    if 'B' in s:
        if minx == -1:
            minx = i
            miny, maxy = s.index('B'), b - s[::-1].index('B') - 1
        maxx = i


# print(maxx, minx, miny, maxy)
print((maxx + minx) // 2 + 1, (maxy + miny) // 2+1 )