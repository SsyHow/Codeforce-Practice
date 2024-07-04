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
tmp = 1
ans = 1
for i in range(1, a):
    if L[i] > L[i-1]:
        tmp += 1
    else:
        ans = max(tmp, ans)
        tmp = 1
ans = max(tmp, ans)
print(ans)