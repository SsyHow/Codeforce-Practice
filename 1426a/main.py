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

for i in range(a):
    x, y = MII()
    if x <= 2:
        print(1)
    else:
        if ((x-2)//y) % 2:
            print((x-2)//y + 2)
        else:
            print((x-2)//y + 1)