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
    x, y = MII()
    s = I()
    if s == s[::-1] or y == 0:
        print(1)
    else:
        print(2)