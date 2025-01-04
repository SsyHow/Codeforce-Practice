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
    m, n = MII()
    ans = 0
    flag = True
    for _ in range(m):
        s = I()
        c = len(s)
        if flag and n >= c:
            n -= c
            ans += 1
        else:
            flag = False
    print(ans)
