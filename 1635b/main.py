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
    b = II()
    L = LII()
    ans = 0
    for i in range(1, b-1):

        if L[i] > L[i-1] and L[i+1] < L[i]:
            if i < b-2:

                L[i+1] = max(L[i], L[i+2])
            else:
                L[i+1] = L[i]
            ans += 1
    print(ans)
    print(*L)