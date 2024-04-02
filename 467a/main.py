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
ans = 0
for i in range(a):
    p, q = MII()
    if q - p >= 2:
        ans += 1
print(ans)