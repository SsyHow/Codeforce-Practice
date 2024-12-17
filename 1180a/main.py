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
tmp = 0
c = 1
while c < a:
    tmp += 4
    ans += tmp
    c += 1
print(ans + 1)