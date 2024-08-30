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
if a % 2:
    print(-1)
else:
    L = list(range(1, a + 1))
    for i in range(0, len(L), 2):
        L[i], L[i+1] = L[i+1], L[i]
    print(' '.join([str(i) for i in L]))