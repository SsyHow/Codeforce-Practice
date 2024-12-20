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
s = I()

ans = ''
for i in s:
    if a % 2 == 0:
        ans = i + ans
    else:
        ans += i

    a -= 1
print(ans)