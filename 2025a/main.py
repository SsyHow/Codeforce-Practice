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
    t = I()
    n = min(len(s), len(t))
    l = 0

    while l < n:
        if s[l] != t[l]:
            break
        l += 1

    print(l + len(s) - l + len(t) - l + 1) if l != 0 else print(len(s) + len(t))
