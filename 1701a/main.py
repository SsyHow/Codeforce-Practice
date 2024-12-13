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
    b = LII()
    c = LII()
    ans = sum(b) + sum(c)

    if ans == 0:
        print(0)
    elif ans == 4:
        print(2)
    else:
        print(1)