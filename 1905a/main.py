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
offset = 1
p0 = 0
ans = ''
while p0 < a:
    ans += s[p0]
    p0 += offset
    offset += 1
print(ans)