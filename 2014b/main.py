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
    if x % 2 == 1:
        if y % 4 == 1 or y % 4 == 2:
            print("NO")
        else:
            print("YES")
    else:
        if y % 4 == 2 or y % 4 == 3:
            print("NO")
        else:
            print("YES")