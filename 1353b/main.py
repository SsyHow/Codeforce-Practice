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
    n, k = MII()
    L1 = LII()
    L2 = LII()
    L1.sort()
    L2.sort(reverse=True)
    b = 0
    while b < k :
        if L1[b] < L2[b]:
            L1[b] = L2[b]
        b += 1
    print(sum(L1))