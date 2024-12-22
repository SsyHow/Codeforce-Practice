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
ans = [0] * b
r = d = 0
for _ in range(a):
    s = I()
    for i in range(b):
        if s[i] == '*':
            ans[i] += 1

    for j in range(1, b):
        if ans[j] > ans[j-1]:
            r = max(r, ans[j] - ans[j-1])
        else:
            d = max(d, ans[j-1] - ans[j])
print(r, d)
