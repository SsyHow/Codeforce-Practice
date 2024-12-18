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
    n, a, b, c, d = MII()
    l1, r1 = n*(a - b), n*(a + b)
    l2, r2 = c - d, c + d

    if l1 <= r2 and l2 <= r1:
        print("YES")
    else:
        print("NO")