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
    if b <= 3:
        print(b - 1)
    elif b % 2 == 1:
        print(3)
    else:
        print(2)
