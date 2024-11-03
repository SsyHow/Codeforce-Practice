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
    b, c, d = MII()
    s = 0
    flag = False
    for i in range(b):
        x, y = MII()
        if flag:
            continue
        elif x - s >= c:
            flag = True
        else:
            s = y
    if not flag and d - s >= c:
        flag = True
    print("YES") if flag else print("NO")