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

    if 0 in L:
        print(b - L.count(0))
    elif len(set(L)) == len(L):
        print(b+1)
    else:
        print(b)
