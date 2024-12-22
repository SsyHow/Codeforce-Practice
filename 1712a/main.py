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
    x, y = MII()
    L = LII()
    ans = 0
    s = set(range(1, y+1))
    for i in range(y):
        if L[i] not in s:
            ans += 1
    print(ans)