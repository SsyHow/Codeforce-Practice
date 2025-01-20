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

    cnt = [[0 for _ in range(b + 1)], [0 for _ in range(b + 1)]]

    for i in range(b):
        cnt[0][i+1] = cnt[0][i] + (L[i] == 0)
        cnt[1][i+1] = cnt[1][i] + (L[i] == 1)

    ans = b-1

    for j in range(b+1):
        ans = min(ans, max(cnt[1][j], cnt[0][b] - cnt[0][j]))
    print(ans)
