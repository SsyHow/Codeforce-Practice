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
    L1= LII()
    L2 = LII()
    ans = 0
    for i in range(1, b):
        if L1[i-1] > L2[i]:
            ans += L1[i-1] - L2[i]
    ans += L1[-1]
    print(ans)