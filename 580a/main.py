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
prev = L[0]
ans, tmp = 1, 1
for i in range(1, len(L)):
    # print(prev, L[i], tmp)
    if prev <= L[i]:

        tmp += 1
    else:
        ans = max(ans, tmp)
        tmp = 1
    prev = L[i]
ans = max(ans, tmp)
print(ans)