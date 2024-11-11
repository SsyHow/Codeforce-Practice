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
    b, c = MII()
    L = LII()
    ans = float('-inf')
    prev = 0
    for i in L:
        ans = max(ans, i - prev)
        prev = i

    ans = max(ans, (c-i) * 2)
    print(ans)