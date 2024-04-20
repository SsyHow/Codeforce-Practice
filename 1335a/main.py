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
    if b< 2:
        print(0)
    elif b % 2:
        print(b//2)
    else:
        print(b//2 - 1)