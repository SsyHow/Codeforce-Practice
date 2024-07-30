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
    x, y = I().split()
    tmp = x
    x = y[0] + x[1:]
    y = tmp[0] + y[1:]
    print(x, y)
