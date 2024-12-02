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
    L = [1]
    cnt = 1
    if k > 1:

        while k ** cnt <= n:
            L.append(k ** cnt)
            cnt += 1
    # print(L)
    ans = 0
    L.reverse()
    for i in L:
        if i > n:
            continue
        ans += n // i
        n = n % i
    print(ans)