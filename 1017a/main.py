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
m = sum(MII())
ans = 1
for _ in range(a-1):
    l = sum(MII())
    if l > m:
        ans += 1
print(ans)