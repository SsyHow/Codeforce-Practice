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

while True:
    if sum(map(int, list(str(a)))) % 4 == 0:
        print(a)
        break
    a += 1
