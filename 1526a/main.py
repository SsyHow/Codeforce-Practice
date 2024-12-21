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

    L1 = L[:b]
    L2 = L[b:]

    ans = []
    for i in range(b):
        ans.append(L1[i])
        ans.append(L2[i])
    print(*ans, sep = ' ')