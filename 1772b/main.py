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
    x, y = MII()
    m, n = MII()
    a = 1 if x > y else 0
    b = 1 if m > n else 0
    c = 1 if x > m else 0
    d = 1 if y > n else 0
    if (a+b) % 2 == 0 and (c+d)% 2 == 0:
        print("YES")
    else:
        print("NO")