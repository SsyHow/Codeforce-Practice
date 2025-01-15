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
    L = []
    for i in range(x):
        b = I()
        for j in range(y):
            if b[j] == 'R':
                L.append((i, j))

    if not L:
        print("NO")
        continue
    p,q = L[0]
    for m, n in L:
        if n < q:
            print("NO")
            break
    else:
        print("YES")