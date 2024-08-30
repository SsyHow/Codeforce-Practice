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
    x, y = MII()
    if x == y:
        print(0)

    elif x > y:
        if (x - y) % 2:
            print(2)
        else:
            print(1)
    else:
        if (y - x) % 2:
            print(1)
        else:
            print(2)
