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

a, b = MII()

if a % 2:
    mid = a // 2 + 1
else:
    mid = a // 2

if b <= mid:
    print(2 * b - 1)
else:
    print((b - mid) * 2)

