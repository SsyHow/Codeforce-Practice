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
    s = list(I())
    t = I()
    ans = 0
    for i in range(b):
        if t[i] == '1':
            if s[i] == '0':
                ans += 1
                s[i] = -1
            elif i > 0 and s[i-1] == '1':
                ans += 1
                s[i-1] = -1
            elif i < b-1 and s[i+1] == '1':
                ans += 1
                s[i+1] = -1

    print(ans)
