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
    M = []
    for i in range(b-1):
        M.append(abs(L[i+1] - L[i]))
    M.sort()

    print(sum(M[:-(c-1)])) if c > 1 else print(sum(M))