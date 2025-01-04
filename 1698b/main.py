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
    m, n = MII()
    L = LII()
    ans = 0
    for i in range(1, m-1):
        if L[i] > L[i - 1] + L[i + 1]:
            ans += 1

    if n == 1:
        print((m - 1) // 2)
    else:
        print(ans)