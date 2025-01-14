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
    j = 1
    L = [0] * b

    for i in range(c-1, b, c):
        L[i] = j
        j += 1
    n = b

    for i in range(b):
        if L[i] == 0:
            L[i] = n
            n -= 1
    print(*L)

