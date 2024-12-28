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
    ans = 0
    tmp = 1
    while c > 0 :
        ans += 1
        c -= b
        tmp = 1 - tmp
        if tmp  == 0:
            b -= 1
    print(ans)