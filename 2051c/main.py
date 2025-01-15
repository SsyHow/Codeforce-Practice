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

t = II()
for _ in range(t):
    n, m, k = MII()
    L = LII()
    M = LII()
    if n == k:
        print('1' * m)
        continue
    if n > k + 1:
        print('0' * m)
        continue
    tmp = sum(range(1, n+1)) - sum(M)

    ans = []
    for i in L:
        if i == tmp:
            ans.append('1')
        else:
            ans.append('0')
    print(''.join(ans))