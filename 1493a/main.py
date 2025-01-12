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
    n, k = MII()
    print(n - k + k //2)

    print(*range((k+1)//2, k), *range(k+1, n+1))