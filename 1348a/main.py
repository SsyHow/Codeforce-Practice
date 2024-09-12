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
    c = 2 ** b
    for i in range(1, b):
        if i < b // 2:
            c += 2 ** i
        else:
            c -= 2 ** i
    print(c)
