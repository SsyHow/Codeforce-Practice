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
    L = sorted(MII())

    i, j, l, k = L[0], L[-2],L[1], L[-1]

    print(abs(i - j) + abs(j - l) + abs(l - k) + abs(i - k))