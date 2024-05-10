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
ans = 1
while ans <= 9:
    if a * ans % 10 == 0 or a * ans % 10 == b:
        break
    ans += 1
print(ans)