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
    mx1 = mx2 = 0
    for i in range(0, b, 2):
        mx1 = max(mx1, L[i])
    for i in range(1, b, 2):
        mx2 = max(mx2, L[i])
    # print(mx1, mx2)
    if mx2 > mx1 and b % 2 == 1:
        print(mx2 + (b + 1) // 2 - 1)
    else:
        print(max(L) + (b + 1) // 2)