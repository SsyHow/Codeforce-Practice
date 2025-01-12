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
    b = II()
    L = LII()
    maxx = float('-inf')
    minx = float('inf')
    x = y = 0
    for idx, i in enumerate(L):
        if i > maxx:
            maxx = i
            x = idx
        if i < minx:
            minx = i
            y = idx
    print(y+1, x+1)