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

x = II()
for _ in range(x):
    a, b, k = MII()
    print((a-b) * (k//2) + a * (k%2))