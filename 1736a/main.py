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

b = II()
for _ in range(b):
    a = II()
    L = LII()
    M = LII()

    ans = sum([1 for i in range(a) if L[i] != M[i]])

    print(min(ans, abs(L.count(1) - M.count(1)) + 1))