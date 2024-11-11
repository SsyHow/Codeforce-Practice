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
for i in range(a):
    b = II()
    s = I().lower()
    s1 = s[0]
    t = 0
    for i in range(1, len(s)):
        if s1[t] != s[i]:
            s1 += s[i]
            t += 1
    if s1 == 'meow':
        print("YES")
    else:
        print("NO")


