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
    if b % 2050 != 0:
        print(-1)
        continue
    else:
        c = b // 2050
        ans = 0
        while c > 0:
            ans += c % 10
            c //= 10
        print(ans)