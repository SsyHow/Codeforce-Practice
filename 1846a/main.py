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
    cnt = 0
    for i in range(b):
        x, y = MII()
        if x > y:
            cnt += 1
    print(cnt)