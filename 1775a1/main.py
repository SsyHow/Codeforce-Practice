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
    if s[1] =='a':
        print(s[0], s[1], s[2:])
    else:
        print(s[0], s[1:-1], s[-1])