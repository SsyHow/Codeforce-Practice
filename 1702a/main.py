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
    b = 0
    c = II()
    while 10 ** b <= c:
        b += 1
    print(c - 10**(b-1))