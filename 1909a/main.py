
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
    x = y = m = n = 0
    for _ in range(b):
        i, j = MII()
        if i > 0:
            x = 1
        elif i < 0:
            y = 1
        if j > 0:
            m = 1
        elif j < 0:
            n = 1
    print("NO" if x + y + m + n == 4 else "YES")