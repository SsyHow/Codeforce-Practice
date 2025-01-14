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
    a,b,c,d,k = MII()
    x = (a + c - 1)//c
    y = (b + d - 1)//d
    if x + y <= k:
        print(x, y)
    else:
        print(-1)