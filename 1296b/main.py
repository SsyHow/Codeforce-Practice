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
    cnt = 0
    while b >= 10:
        cnt += b // 10 * 10
        b = b // 10 + b % 10

    cnt += b
    print(cnt)
