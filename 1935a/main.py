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
    _ = II()
    b = I()
    c = b[::-1]
    if c < b:
        print(c+b)
    else:
        print(b)