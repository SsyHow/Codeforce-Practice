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
    print(b * 4 + (2 + b-2) * (b-2 - 2 + 1) + 3 + b-1)