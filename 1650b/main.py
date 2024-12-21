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
    l, r, x = MII()

    ans = r // x + r % x
    m = r // x * x - 1

    if m >= l:
        ans = max(ans, m // x + m % x)
    print(ans)
