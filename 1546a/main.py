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
    L1 = LII()
    L2 = LII()

    if sum(L1) != sum(L2):
        print("-1")
        continue
    ans = []
    p = []
    q = []
    k = [L1[i] - L2[i] for i in range(b)]

    for i in range(b):
        if k[i] > 0:
            p.extend([i+1] * k[i])
        elif k[i] < 0:
            q.extend([i+1] * (-k[i]))
    print(c :=len(p))
    for i in range(c):
        print(p[i], q[i])







