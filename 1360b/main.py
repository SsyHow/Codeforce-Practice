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
for i in range(a):
    b = II()
    L = LII()
    L.sort()
    M = [0] * (b-1)

    for j in range(1, b):
        M[j-1] = L[j] - L[j-1]
    print(min(M))