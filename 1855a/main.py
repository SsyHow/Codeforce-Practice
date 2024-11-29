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
    L = LII()
    cnt = 0
    for idx, i in enumerate(L):
        # print(idx, i)
        if idx+1 == i:
            cnt += 1
    print((cnt + 1)//2)