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

n = II()
for _ in range(n):
    s = I()
    a= s[0]
    tmp = 0
    for i in range(1, len(s)):
        if a > s[i]:
            a = s[i]
            tmp = i
    print(a, ''.join([s[:tmp], s[tmp+1:]]))

