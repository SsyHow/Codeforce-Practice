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
    a, b, c, x, y= MII()
    if max(x-a, 0) + max(y-b,0) <= c:
        print("YES")
    else:
        print("NO")