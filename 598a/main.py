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
    s = II()

    a = (1 + s) * s // 2
    k = 1
    while k <= s:
        a -= k * 2
        k *= 2
    print(a)