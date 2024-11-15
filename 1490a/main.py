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
    ans = 0
    for i in range(b-1):
        x, y = min(L[i], L[i+1]), max(L[i], L[i+1])
        while x*2 < y:
            x *= 2
            ans += 1
    print(ans)