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
p = [II() for i in range(a)]
ans = 0
for i in range(a):
    g = 0
    while i >= 0:
        g += 1
        i = p[i] - 1

    ans = max(ans, g)
print(ans)