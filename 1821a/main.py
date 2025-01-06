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
    s = I()
    n = len(s)
    ans = 1
    for i in range(n):

        if s[i] == '?':
            ans *= 9 if i == 0 else 10
        if s[0] == '0':
            ans = 0
            break
    print(ans)
