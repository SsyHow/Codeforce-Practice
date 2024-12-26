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
    n, b, x, y = MII()
    ans = a1 = 0
    for _ in range(n):
        if a1 + x > b:
            a1 -= y
            ans += a1
        else:
            a1 += x
            ans += a1
    print(ans)
