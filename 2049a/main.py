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
    L = LII()

    ans = 0
    Flag = True
    for i in L:
        if Flag and i > 0:
            ans += 1
            Flag = False
        elif i == 0:
            Flag = True
    if ans == 0:
        print(0)
    elif ans == 1:
        print(1)
    else:
        print(2)

