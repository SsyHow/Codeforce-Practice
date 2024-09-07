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
for i in range(a):
    a, b, c = MII()
    n = 2 * abs(a-b)
    if a > n or b > n or c > n:
        print(-1)
        continue
    d1 = c + n // 2
    d2 = c - n // 2
    # print(d1,d2,n)
    a = [j for j in [d1,d2] if 1<= j <= n]
    if a :
        print(a[0])
