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
    lena = II()
    L = LII()
    L.sort()
    L[0] += 1
    ans = 1
    for i in L:
        ans *= i
    print(ans)