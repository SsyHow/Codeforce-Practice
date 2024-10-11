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
    b, c = MII()
    if b == 0:
        print(1)
    else:
        print(c*2 + b + 1)
