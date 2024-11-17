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
    _ = I()
    a1, a2 = MII()
    b1, b2 = MII()
    c1, c2 = MII()
    if a1 == b1:
        dis = abs(a2 - b2)
        if c1 == a1 and (a2 <= c2 <= b2 or a2 >= c2 >= b2):
            dis += 2
        print(dis)
    elif a2 == b2:
        dis = abs(a1 - b1)
        if c2 == a2 and (a1 <= c1 <= b1 or a1 >= c1 >= b1):
            dis += 2
        print(dis)
    else:
        print(abs(a1 - b1) + abs(a2 - b2))