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
    L = LII()
    L.sort()

    prev = L[0]
    p0 = 0
    for i in L:
        if i != prev:
            break

        p0 += 1
    x = L[:p0]
    y = L[p0:]
    if not y:
        print(-1)
    else:
        print(len(x), len(y))
        print(' '.join([str(i) for i in x]))
        print(' '.join([str(i) for i in y]))

