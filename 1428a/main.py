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
    x, y, m, n = MII()
    if x == m or y == n:
        print(max(abs(x-m), abs(y - n)))
    else:
        print(abs(x - m) + abs(y - n) + 2)