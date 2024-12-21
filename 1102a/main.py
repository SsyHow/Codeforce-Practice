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
if a % 4 == 0 or a % 4 == 3:
    print(0)
else:
    print(1)