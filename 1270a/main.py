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
    b = LII()
    c = LII()
    d = LII()

    print("YES" if max(c) > max(d) else "NO")