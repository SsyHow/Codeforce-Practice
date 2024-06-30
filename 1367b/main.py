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

    b = II()
    L = LII()
    ans1, ans2 = 0, 0
    for idx, i in enumerate(L):
        if idx % 2 == 0:
            ans1 += i % 2
        else:
            ans2 += (i+1) % 2
    if ans1 == ans2:
        print(ans1)
    else:
        print(-1)
