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
    L.sort()
    ans = b - 2
    j = 0
    for i in range(2, b):
        while L[j] + L[j+1] <= L[i]:
            j += 1

        ans = min(ans, b - 1 - i + j)
    print(ans)



