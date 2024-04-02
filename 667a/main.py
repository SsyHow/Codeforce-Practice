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
c = LII()
ans = 0
for i in c:
    if i <= b:
        ans += 1
    else:
        ans += 2
print(ans)