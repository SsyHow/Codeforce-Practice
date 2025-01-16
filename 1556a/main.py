
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
    c, d = MII()

    if abs(c - d) & 1 == 1:
        print(-1)
    elif c == d == 0:
        print(0)
    elif c == d:
        print(1)
    else:
        print(2)
