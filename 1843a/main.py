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
    L = sorted(LII())
    cnt = 0
    for i in range(b//2):
        cnt += L[b-i-1] - L[i]
    print(cnt)