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
prev = s[0]
ans = 0
for i in s[1:]:
    if i != prev:
        if i == "F":
            ans += 1
        else:
            ans -= 1
        prev = i

print("YES" if ans > 0 else "NO")