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

a = I().lower()
b = I().lower()


if a == b:
    print(0)
elif a < b:
    print(-1)
else:
    print(1)
