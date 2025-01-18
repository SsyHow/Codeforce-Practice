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
    b, c, d = MII()
    x = min(b, c//2)

    ans1 = x * 3 + min(c - 2 * x, d//2) * 3
    # print(ans1)

    y = min(c, d//2)
    ans2 = min(b, (c - y )//2) * 3 + y * 3
    # print("*", (b, (c - y * )//2, y))
    print(max(ans1, ans2))

