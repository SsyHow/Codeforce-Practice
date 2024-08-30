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
ans = 0
for i in range(1, a // 2 + 1):
    if (a - i) % i == 0:
        ans += 1
print(ans)