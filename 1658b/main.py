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
mod =  998_244_353
for _ in range(a):
    b = II()
    ans = 1
    if b & 1 == 0:
        for i in range(1, b//2 + 1):
            ans *= i * i
            ans %= mod
        print(ans)

    else:
        print(0)

