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

s = 'abcdefghijklmnopqrstuvwxyz'
a = II()
for _ in range(a):
    n, k = MII()
    print(s[:k] * n)
