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

    if (x-1) // 2 < y:
        print(-1)
        continue

    i, j = 1, -1
    L = list(range(1, x + 1))
    M = [0] * x
    while y > 0:
        M[i] = L[j]
        i += 2
        j -= 1
        y -= 1
    c = 0
    for i in range(x):
        if M[i] == 0:
            M[i] = L[c]
            c += 1

    print(*M)
