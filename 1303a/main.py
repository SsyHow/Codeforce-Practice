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
    b = I()
    p0, p1 = 0, len(b) - 1
    while p0 < p1 and b[p0] != '1':
        p0 += 1
    while p0 < p1 and b[p1] != '1':
        p1 -= 1

    print(b[p0:p1].count('0'))
