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

p = float('-inf')
ans = 1
for i in MII():
    if i - p > b:
        ans = 1
    else:
        ans += 1
    p = i
print(ans)