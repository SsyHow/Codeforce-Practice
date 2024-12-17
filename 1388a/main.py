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
    b = II()
    if b < 31:
        print("NO")
    else:
        print("YES")
        if b - 6 - 10 -14 in {6, 10, 14}:
            print(6, 10, 15, b - 6 - 10 - 15)
        else:
            print(6, 10, 14, b - 6 - 10 -14)