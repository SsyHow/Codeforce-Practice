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
    if len(s) == 2:
        print(s[1])
    else:
        print(min(list(s)))