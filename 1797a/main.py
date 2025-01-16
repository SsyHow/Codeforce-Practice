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
    m, n = MII()

    x1, y1, x2, y2 = MII()
    k = j = 4
    if x1 == 1 or x1 == m:
        k -= 1
    if x2 == 1 or x2 == m:
        j -= 1
    if y1 == 1 or y1 == n:
        k -= 1
    if y2 == 1 or y2 == n:
        j -= 1

    print(min(k,j))
