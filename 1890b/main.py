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

def f(n, s):
    for i in range(n-1):
        if s[i] == s[i+1]:
            return False
    return True


a = II()
for _ in range(a):
    b, c = MII()
    s = I()
    t = I()

    if f(b, s):
        print("YES")
        continue

    if not f(c, t):
        print("NO")
        continue

    for i in range(b-1):
        if s[i] == s[i + 1]:
            if s[i] == t[0] or s[i+1] == t[-1]:
                print("NO")
                break
    else:
        print("YES")
