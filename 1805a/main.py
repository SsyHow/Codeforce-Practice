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
    s = II()
    L = LII()
    ans = 0
    for i in L:
        ans ^= i

    if s % 2 == 0 and ans > 0:
        print(-1)
    else:
        print(ans)

