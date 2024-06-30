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
    a,b = MII()
    c,d = MII()
    x = 1 if a > b else 0
    y = 1 if c > d else 0

    if x ^ y:
        print("NO")
    else:
        print("YES")