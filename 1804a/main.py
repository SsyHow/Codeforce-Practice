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
    b, c = sorted(map(abs, MII()))
    if b + 1 >= c:
        print(b+c)
    else:
        print((c - (b+1)) * 2 + 2 * b + 1)