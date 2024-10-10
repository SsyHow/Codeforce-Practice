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
    c = sum(L)
    if c == b:
        print(0)
    elif c < b:
        print(1)
    else:
        print(c - b)
