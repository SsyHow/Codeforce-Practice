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
    n,f, k = MII()
    L = LII()
    f = L[f-1]
    L.sort(reverse=True)
    # print(f, L[k], L.count(f) )
    # print(L)
    if n <= k or L[k] < f:
        print("YES")
    elif L[k] == f and L[k-1]== f:
        print("MAYBE")
    else:
        print("NO")