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
    b, c = MII()
    if c <= (2 * b - 2) * 2:
        print((c + 1)//2)
    else:
        print(c// 2 + 1)