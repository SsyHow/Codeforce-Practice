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
    x, y, z = MII()
    s1 = sorted(I())
    s2 = sorted(I())

    c = []
    p = q = t1 = t2 = 0

    while p < x and q < y:
        if s1[p] <= s2[q] and t1 < z:
            c.append(s1[p])
            p += 1
            t1 += 1
            t2 = 0
        elif t1 == z:
            c.append(s2[q])
            q += 1
            t2 += 1
            t1 = 0
        elif s1[p] > s2[q] and t2 < z:
            c.append(s2[q])
            q += 1
            t2 += 1
            t1 = 0
        elif t2 == z:
            c.append(s1[p])
            p += 1
            t1 += 1
            t2 = 0
    print(''.join(c))
