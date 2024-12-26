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
    ans = 0
    a2 = a3 = a5 = 0
    while b % 5 == 0:
        a5 += 1
        b //= 5

    while b % 3 == 0:
        a3 += 1
        b //= 3

    while b % 2 == 0:
        a2 += 1
        b //= 2

    if b != 1:
        print(-1)
    else:
        print(a2 + 2 * a3 + 3 * a5)


