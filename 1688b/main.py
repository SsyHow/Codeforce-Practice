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

def f(k):
    p = 0
    while k > 0:
        if k & 1 == 1:
            return p
        p += 1
        k >>= 1


a = II()
for _ in range(a):
    b = II()
    L = LII()

    emin = float('inf')
    e = 0
    for i in L:
        if i & 1 == 0:
            e += 1
        # print(f(i),"***")
        emin = min(emin, f(i))
    if e == 0:
        print(0)
    elif e == b:
        print(emin + e - 1)
    else:
        print(e)
