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
mx = 0
cur = 0
for i in range(a):
    b, c = MII()
    cur = cur - b + c
    mx = max(mx, cur)
print(mx)