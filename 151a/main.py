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

n, k, l, c, d, p, nl, np = MII()

print(min(k*l//nl//n, c*d//n, p//np//n) )

