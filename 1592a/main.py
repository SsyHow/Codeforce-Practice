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
    b, c = MII()
    L = sorted(MII(), reverse=True)

    p1 = L[0]
    p2 = L[1]

    p = p1 + p2

    ans = c // p * 2
    res = c % p

    if res > 0:
        ans += 1
        if res > p1:
            ans +=  1
    print(ans)

