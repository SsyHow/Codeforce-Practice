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
    n, s, r = MII()
    mx = s - r
    L = [mx] + [1] * (n-1)
    i = 1
    s = s - mx - (n - 1)
    # print(s)
    while s > 0:
        L[i] = min(s+L[i], mx)
        s -= L[i] - 1
        i += 1
    for i in L:
        print(i, end = ' ')
    print()
