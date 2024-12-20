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
    n = II()
    a = [0]
    for i in MII():
        a.append(a[-1] + i)

    s = I()
    ans = 0
    l, r = 0, n - 1

    while r > l:
        while l < n and s[l] == 'R':
            l += 1
        while r >= 0 and s[r] == 'L':
            r -= 1

        if l < r:
            ans += a[r+1] - a[l]
            l += 1
            r -= 1
    print(ans)
