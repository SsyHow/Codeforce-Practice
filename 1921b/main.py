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
    n = II()
    b = I()
    c = I()
    l = r = 0
    for i in range(n):
        if b[i] > c[i]:
            l += 1
        elif b[i] < c[i]:
            r += 1
    print(max(l, r))