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
    l, r = MII()
    id = 1

    cnt = 0

    while l <= r:
        # print(l, end = ' ')
        l += id
        id += 1
        cnt += 1
    print(cnt)