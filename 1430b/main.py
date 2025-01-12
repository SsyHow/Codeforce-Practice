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
    b, c = MII()
    L = sorted(MII())

    if c > 0:
        print(sum(L[-1*c - 1:]))
    else:
        print(max(L) - min(L))