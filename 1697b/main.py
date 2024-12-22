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

a, b = MII()
L = LII()
L.sort()
ans = [0] * (a + 1)

for i in range(a):
    ans[i+1] = ans[i] + L[i]
# print(L)

for _ in range(b):
    x, y = MII()

    print(ans[a-x+y] - ans[a - x])
