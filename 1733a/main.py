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
    b, c = MII()
    L = LII()
    ans = 0
    for i in range(c):
        tmp = 0
        for j in range(b):
            if j % c == i:
                # print(tmp, L[j], i)
                tmp = max(tmp, L[j])
        ans += tmp
    print(ans)
