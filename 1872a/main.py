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
    x, y, z = MII()
    x, y = min(x, y), max(x, y)
    cnt = 0
    while x < y:
        # print(x, y)
        x += z
        y -= z
        cnt += 1

    print(cnt)