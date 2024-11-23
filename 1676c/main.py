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


def diff(s: str, t:str, c):
    cnt = 0
    for i in range(c):
        cnt += abs(ord(s[i]) - ord(t[i]))
    # print(cnt)
    return cnt
a = II()
for i in range(a):
    b, c = MII()
    s = [''] * b
    ans = float('inf')
    for i in range(b):
        s[i] = I()

    for i in range(b):
        for j in range(i+1, b):
            ans = min(ans, diff(s[i], s[j], c))
    print(ans)