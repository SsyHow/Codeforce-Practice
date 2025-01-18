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
    ans = 0
    if s == '^':
        print(1)
        continue
    if s[0] != '^':
        ans += 1
    if s[-1] != "^":
        ans += 1

    s = s.split('^')
    for i in s:
        if i:
            ans += len(i) - 1
    print(ans)