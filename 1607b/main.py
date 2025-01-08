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
    b, c = MII()
    i = c // 4 * 4
    x = ans = 0 if b & 1 == 0 else 1
    while i < c:
        i += 1
        ans = ans + i if ans & 1 == 1 else ans - i
        # i += 1

        # print(i, c, ans)
    print(ans + b - x)
