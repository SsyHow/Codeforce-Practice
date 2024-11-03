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
    Flag = True
    for _ in range(b):
        c = I()
        if c.count('1') == 1:
            Flag = False
    if Flag:
        print("SQUARE")
    else:
        print("TRIANGLE")
