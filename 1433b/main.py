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
    s = LI()
    l, r = 0, b-1

    while s[l] != '1':
        l += 1
    while s[r] != '1':
        r -= 1

    print(s[l:r+1].count('0'))