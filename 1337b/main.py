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
    x, m, n = MII()

    while m and x > n * 10:
        x = x // 2 + 10
        m -= 1

    if x <= n * 10:
        print("YES")
    else:
        print("NO")