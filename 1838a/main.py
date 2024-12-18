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
    c = float('inf')
    for i in L:
        if i < 0:
            c = i
    print(max(L)) if c > 0 else print(c)