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
    n, m, k, H = MII()
    L = LII()
    cnt =0
    for i in L:
        if H == i:
            continue
        x = abs(H-i)
        if x % k == 0 and x // k <= m-1:
            # print(H, i, x, k)
            cnt += 1
    print(cnt)
