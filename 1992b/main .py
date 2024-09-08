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

a =  II()
for i in range(a):
    n ,k = MII()
    L = LII()
    L.sort()
    cnt = 0
    for i in L[:-1]:
        if i == 1:
            cnt += 1
        if i != 1:
            cnt += i - 1 + i

    print(cnt)