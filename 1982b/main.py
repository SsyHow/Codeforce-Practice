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
    x, y, k = MII()
    while k > 0 and x != 1:
        ans = (x//y + 1) * y - x
        ans = min(ans, k)
        x += ans
        while x % y == 0:
            x //= y
        k -= ans
    print(x + k % (y - 1))
