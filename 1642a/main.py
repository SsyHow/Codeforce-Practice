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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a = II()
for _ in range(a):
    x1, y1 =MII()
    x2, y2 = MII()
    x3, y3 = MII()

    if y1 == y2 and y3 < y2:
        print(abs(x1- x2))

    elif y2 == y3 and y1 < y3:
        print(abs(x2 - x3))
    elif y1 == y3 and y2 < y1:
        print(abs(x1 - x3))
    else:
        print(0)