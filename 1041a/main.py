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
# for _ in range(a):
L = LII()
l, h = min(L), max(L)

print(h-l + 1 - a)
