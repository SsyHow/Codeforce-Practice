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

    s1 = s2 = 0

    for i in range(b):
        if i & 1 == 1 and L[i] > 0:
            s1 += L[i]
        elif i & 1 == 0 and L[i] > 0:
            s2 += L[i]

    print(max(s1, s2)) if s1 > 0 or s2 > 0 else print(max(L))