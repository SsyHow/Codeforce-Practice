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
    b, k = MII()
    L = LII()
    M = LII()
    Z = sorted(zip(L, M))

    for i in range(b):
        if k < Z[i][0]:
            print(k)
            break
        else:
            k += Z[i][1]
    else:
        print(k)