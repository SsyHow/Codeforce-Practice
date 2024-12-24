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
L.append(1)
ans = []
tmp = 1
for i in range(1, a+1):
    if L[i] <= L[i-1]:
        ans.append(L[i-1])
print(len(ans))
print(*ans, sep = ' ')