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

a,b = MII()

ans = 0
while a <= b:
    a *= 3
    b *= 2
    ans += 1
print(ans)