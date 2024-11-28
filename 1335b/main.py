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
s = 'qwertyuiopasdfghjklzxcvbnm'
for _ in range(a):
    n, x, y = MII()
    d = n // y  + 1
    print((s[:y] * d)[:n])