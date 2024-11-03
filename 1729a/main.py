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
    a, b, c = MII()
    # print(abs(a - 1) , (abs(b-c) + abs(c - 1)))
    if abs(a - 1) < (abs(b-c) + abs(c - 1)):
        print(1)

    elif abs(a - 1) == (abs(b-c) + abs(c - 1)):
        print(3)
    else:
        print(2)