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
    if x % 2 == 1:
        print("NO")
    elif y % 2 != 0 and x < 2:
        print("NO")
    else:
        print("YES")