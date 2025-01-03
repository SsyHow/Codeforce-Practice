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
for _ in range(a):
    b = II()
    s = I()
    ans = 0
    for i in range(b):
        if i != b-1 and s[i] != '0':
            ans += int(s[i]) + 1
        elif s[i] != '0':
            ans += int(s[i])
    print(ans)