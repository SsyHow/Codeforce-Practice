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
    ans = n
    i = 1
    while i * i <= n and i <= k:
        if n % i == 0:
            if n // i <= k:
                ans = i
                break
            ans = min(ans, n // i)
        i += 1
    print(ans)



