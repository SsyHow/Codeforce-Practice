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
b = LII()
maxe = max(b)
ans = 0
for i in b:
    ans += maxe - i

print(ans)


