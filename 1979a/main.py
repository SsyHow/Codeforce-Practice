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
    n = II()
    L = LII()
    low = float('inf')
    for i in range(1, n):
        low = min(max(L[i], L[i-1]), low)
    print(low - 1)