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
    x = '##'
    y = '..'
    b = II()
    for i in range(2 * b):
        if i % 4 < 2:
            if b % 2:
                print((x+y)* (b//2) + x)
            else:
                print((x+y) * (b//2))
        else:
            if b % 2:
                print((y+x)*(b//2) + y)
            else:
                print((y+x) * (b//2))