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
    L = LII()
    M = LII()

    v = -1
    k = -2
    for i in range(b):
        tmp = i + L[i]
        if tmp > c:
            continue
        if M[i] > v:
            v = M[i]
            k = i
    print(k + 1)