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
    for i in range((b-1)//2, -1, -1):
        if s[i] == s[(b-1)//2]:
            ans += 1
        else:
            break
    print(ans*2 if b & 1 == 0 else ans*2 - 1)
