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


for _ in range(II()):

    p0 = 0
    p1 = 1
    b = II()
    c = I()
    s = ''
    while p1 < b:
        if c[p0] == c[p1]:
            s += c[p0]
            p0 = p1 + 1
            p1 += 1
        p1 += 1
    print(s)