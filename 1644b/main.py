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


    for i in range(1, b):
        L = [i]
        s = (1 + b) * b // 2
        curmax = b
        s -= i
        vis = {i}
        while s > 0:
            L.append(curmax)
            vis.add(curmax)
            s -= curmax
            while curmax in vis:
                curmax -= 1

        print(*L)
    print(*range(b, 0, -1))