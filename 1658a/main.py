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
    for i in range(b-1):
        if s[i:i+3] == '010':
            ans += 1
        elif s[i:i+2] == '00':
            ans += 2
    print(ans)