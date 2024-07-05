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
    b = II()
    L = LII()
    n = 0
    for i in L:
        if i % 2:
            n += 1
    if n % 2 == 0:
        print("YES")
    else:
        print("NO")