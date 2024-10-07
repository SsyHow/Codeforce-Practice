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
b = I()
ans , cnt = 0, 0
for i in b:
    if i == 'x':
        cnt += 1
    else:
        ans += max(cnt-2, 0)
        cnt = 0

ans += max(cnt-2, 0)
print(ans)
