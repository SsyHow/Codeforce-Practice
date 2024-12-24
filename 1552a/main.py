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
    s = I()

    L = list(s)
    M = sorted(L)
    ans = 0
    for i in range(b):
        if L[i] != M[i]:
            ans += 1
    print(ans)