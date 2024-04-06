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
# a = 74
cnt = 0
if a >= 100:
    cnt += a//100
    a %= 100
if a >= 20:
    cnt += a//20
    # print(cnt)
    a %= 20
if a >= 10:
    cnt += a//10
    # print(cnt)
    a %= 10
if a >= 5:
    cnt += a//5
    # print(cnt)
    a %=5
if a != 0:
    # print(cnt)
    cnt += a
print(cnt)