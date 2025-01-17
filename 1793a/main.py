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

t = II()
for _ in range(t):
    a, b = MII()
    n, m = MII()

    print(min(a*n, b*n, (n // (m+1) * a * m + min(a, b) * (n %(m+1)))))