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
    b, p, f = MII()
    h, c = MII()

    if h > c:
        nump = min(p, b//2)
        numf = min((b-nump*2) //2, f)
        print(nump * h + numf* c)

    else:
        numf = min(f, b // 2)
        nump = min((b - numf * 2) // 2, p)
        print(nump * h + numf * c)

