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
    i = 0

    M = sorted(L)

    while L != M:
        # print(L, M)
        if i & 1 == 0 :

            for j in range(0, b-2, 2):
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
        else:
            for j in range(1, b-1, 2):
                if L[j] > L[j+1]:
                    L[j], L[j+1] = L[j+1], L[j]
        i += 1
    print(i)