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
    b, c = MII()
    b1 = I()
    c1 = I()
    cnt = 0
    flag = c1 not in b1
    while flag and cnt <=6:
        b1 *= 2
        cnt += 1
        flag = c1 not in b1
        # print(c1, b1)
    print(cnt) if not flag else print(-1)