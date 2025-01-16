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
L = LII()
cnt = L.count(1)
for _ in range(b):
    x, y = MII()
    if x == 1:
        if L[y-1] == 0:
            cnt += 1
        else:
            cnt -= 1
        L[y - 1] = 1 - L[y - 1]

    else:
        print(1 if cnt >= y else 0)