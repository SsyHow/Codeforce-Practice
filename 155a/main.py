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
curmax = L[0]
curmin = L[0]
ans = 0
for i in L[1:]:
    if i > curmax:
        curmax = i
        ans += 1
    if i < curmin:
        curmin = i
        ans += 1

print(ans)