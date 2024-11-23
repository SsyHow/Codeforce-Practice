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
    b, c = MII()
    if b > c:
        b, c = c, b
    if b * 3 <= c:
        print(b)
    else:
        print( (c+b) // 4)
