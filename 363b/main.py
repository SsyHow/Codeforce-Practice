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

a, b = MII()
L = LII()
cnt = 0
ans = tmp = sum(L[:b])

for i in range(1, a-b + 1):
    # print(ans, tmp, L[i-1], L[i+b-1])
    if tmp > ans - L[i-1] + L[i+b-1]:
        cnt = i
        tmp = ans - L[i-1] + L[i+b-1]
    ans = ans - L[i-1] + L[i+b-1]

print(cnt + 1)