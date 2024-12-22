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
L = LII()

zeros = L.count(0)
neg = 0

ans = 0
for i in L:
    if i < 0:
        ans += -1 - i
        neg += 1
    elif i > 0:
        ans += i - 1

if zeros > 0:
    ans += zeros
elif neg % 2 == 1:
    ans += 2
print(ans)