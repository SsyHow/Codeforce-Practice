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
    b, c = MII()
    L = []
    for _ in range(b):
        L.append(I())
    for i in range(0, b, c):

        for j in range(0, b, c):
            print(L[i][j], end = '')
        print()