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

    mx = max(L)
    idx = -1
    for i in range(b):
        if L[i] != mx: continue
        # print(i, b-1, L[i])
        if (i > 0 and L[i-1] < mx) or (i < (b-1) and L[i+1] < mx):
            idx = i + 1
            print(idx)
            break
    else:
        print(idx)