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
cur = abs(L[a-1] - L[0])
ans = a
for i in range(a-1):
    if abs(L[i] - L[i+1]) < cur:
        ans = i
        cur = abs(L[i] - L[i+1])
if ans == a:
    print(a, 1)

else:
    print(ans+1, ans +2)

