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
    if sum(L) % b > 0:
        print("NO")
    else:
        c = sum(L) // b
        M = [L[j] for j in range(0, b, 2)]
        nM = len(M)
        K = [L[j] for j in range(1, b, 2)]
        nK = len(K)
        if sum(M) / nM == sum(K) / nK == c:
            print("YES")

        else:
            print("NO")