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
L = LII()
L.sort()
ans = 0
for i in range(0, a, 2):
    ans += L[i+1] - L[i]
print(ans)