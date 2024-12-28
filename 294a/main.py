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
L = LII()
b = II()
for i in range(b):
    x, y = MII()
    x -= 1

    if x > 0:
        L[x - 1] += y - 1
    if x < a-1:
        L[x+1] += L[x] - y
    L[x] = 0
print(*L, sep='\n')