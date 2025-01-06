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
ans = [0] * 10
l, r = 0, 10 - 1
s = I()
for i in s:
    if i == 'L':
        while ans[l] == 1:
            l += 1

        ans[l] = 1
    elif i == "R":
        while ans[r] == 1:
            r -= 1
        ans[r] = 1
    else:
        i = int(i)
        ans[i] = 0
        if i < l:
            l = i
        if i > r:
            r = i
print(*ans, sep='')