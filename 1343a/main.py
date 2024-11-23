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
    for i in range(2, 30):
        if b % (2 ** i - 1) == 0:
            print(b//(2 ** i -1))
            break