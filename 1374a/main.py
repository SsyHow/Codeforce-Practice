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
    if (c - c//a*a) < b:
        print((c//a - 1) * a + b)
    else:
        print(c//a * a + b)
