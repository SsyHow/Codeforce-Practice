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
    r, b, d = MII()
    if r > b:
        r, b = b, r
    if r * (d) >= b-r:
        print("YES")
    else:
        print("NO")