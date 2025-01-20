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

a, b, c = MII()
ans = 0
for i in range(1, c+1):
    if i % a == 0 and i % b == 0:
        ans += 1
print(ans)