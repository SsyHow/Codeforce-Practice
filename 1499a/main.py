
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
    n, k1, k2 = MII()
    w, b = MII()
    nw = k1 // 2 + k2 // 2 + 1 if k1 & 1 == k2 & 1 == 1 else k1 // 2 + k2 // 2
    nb = n - nw if k1 & 1 == k2 & 1 else n - nw - 1
    print("YES") if nw >= w and nb >= b else print("NO")