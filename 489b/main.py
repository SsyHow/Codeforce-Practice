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
b = II()
M = LII()
L.sort()
M.sort()

l = r = 0
ans = 0
while l < a and r < b:
    if abs(L[l] - M[r]) <= 1:
        l += 1
        r += 1

        ans += 1
    elif L[l] > M[r]:
        r += 1
    else:
        l += 1
print(ans)