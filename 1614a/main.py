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
    n, l, r, k = MII()

    L = LII()
    M = []
    for i in L:
        if l <= i <= r:
            M.append(i)

    M.sort()
    j = len(M) - 1
    xxx = sum(M)
    ans = len(M)
    # print(M, ans)
    while xxx > k:
        xxx -= M[j]
        j -= 1
        ans -= 1
    print(ans)