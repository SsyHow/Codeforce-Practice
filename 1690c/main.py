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
    L = LII()
    M = LII()

    tmp = 0
    ans = []
    for i in range(b):
        ans.append(str(M[i] - max(tmp, L[i])))
        tmp = M[i]
    print(' '.join(ans))