
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
    p = q = m = n = 0
    for _ in range(b):
        x, y = MII()
        p = max(p, x)
        q = max(q, y)
        m = min(x, m)
        n = min(y, n)
    print(2 * (p+q - m- n))
