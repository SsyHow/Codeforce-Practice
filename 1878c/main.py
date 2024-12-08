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
    n, k, x = MII()
    mx = (n + (n+1 - k)) * k //2
    mi = (1 + k) * k // 2

    if mi <= x <= mx:
        print("YES")
    else:
        print("NO")