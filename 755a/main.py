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
if a == 2:
    print(4)
elif a & 1 == 1:
    print(3)
else:
    print(a - 2)