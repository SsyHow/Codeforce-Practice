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

a, t = MII()
L = LII()

p2 = len(L) - 1
tmp, cnt = 0, 0
ans = 0
for i in range(a-1, -1, -1):
    tmp += L[i]
    cnt += 1

    while tmp > t:
        tmp -= L[p2]
        p2 -= 1
        cnt -= 1

    ans = max(cnt, ans)
print(ans)
