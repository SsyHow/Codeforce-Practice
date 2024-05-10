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

n,k = MII()

c = LII()
ans = len(c)
for i in c:
    if i > 5-k:
        ans -= 1
print(ans//3)