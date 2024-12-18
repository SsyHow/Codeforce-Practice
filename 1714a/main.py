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
    b, s1, s2 = MII()

    n = 60 * s1 + s2
    ans = float('inf')
    for _ in range(b):
        x, y = MII()
        n1 = x * 60 + y

        ans = min(ans, 24 * 60 - n + n1) if n1 < n else min(ans, n1 - n)
        # print(ans)
    print(ans//60, ans % 60)
