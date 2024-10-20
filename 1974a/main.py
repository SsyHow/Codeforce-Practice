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
# from math import ceil
a = II()
for _ in range(a):
    x,y = MII()
    cnt = 0
    #y>2
    if y >= 2:
        cnt += y // 2

        x -= 7 * (y//2)
        y %= 2
    # print(cnt, y,x)
    if y == 1:
        cnt += 1
        y -= 1
        x -= 11
    if x > 0 :
        cnt += x//15 + 1 if x%15 else x//15
        # x -= -15 * (x//15)

    print(cnt)