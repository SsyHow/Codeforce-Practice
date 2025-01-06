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
t = I()
ans = 0
i = 0
while i < a:
    if i < a - 1 and ((s[i:i+2] == '01' and t[i:i+2] == '10') or (s[i:i+2] == '10' and t[i:i+2] == '01')):
        ans += 1
        i += 1
    elif s[i] != t[i]:
        ans += 1

    i += 1
print(ans)
