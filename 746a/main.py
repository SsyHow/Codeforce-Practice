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

l = II()
a = II()
p = II()

print(min(l, a // 2, p // 4) * 7)