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

a,b = MII()

c = 6 - max(a, b) + 1

if c == 1:
    print("1/6")
elif c == 2:
    print("1/3")
elif c == 3:
    print("1/2")
elif c == 4:
    print("2/3")
elif c == 5:
    print("5/6")
elif c == 6:
    print("1/1")
