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

    for i in range(b-1):
        if L[i] > L[i+1]:
            ans = max(ans, L[i])
    print(ans)