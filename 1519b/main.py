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
x = II()
for i in range(x):
    a,b,c = MII()
    # print((a - 1) + b * (a-1))
    if (b - 1) + (b) * (a-1) == c:
        print("YES")
    else:
        print("NO")