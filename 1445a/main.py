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
for k in range(a):
    m, n = MII()
    L = LII()
    M = sorted(MII(), reverse=True)

    for i in range(m):
        if L[i] + M[i] > n:
            print('NO')
            break
    else:
        print("YES")
    if k!= a-1:
        s = I()


