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
    L = sorted(MII(), reverse=True)

    a = b = 0

    for i in L:
        a += i
        if a >= c:
            break
        b += i

    if a == c:
        print(0)
    else:
        print(c - b)
