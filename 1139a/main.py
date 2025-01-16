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
s = I()
ans = 0
for i in range(a):
    if s[i] in '24680':
        ans += (i+1)
print(ans)