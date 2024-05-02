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
    b = LII()
    ans = 0
    p = b[0]
    for j in b[1:]:
        if j > p:
            ans += 1
    print(ans)
