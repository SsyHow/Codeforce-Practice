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
    x = I()
    cnt = 0
    l, r = 0, len(x) - 1
    while x[l] == 'W':
        cnt += 1
        l += 1
    while l < r and x[r] == 'W':
        cnt += 1
        r -= 1
    print(b - cnt)