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
    i = 1
    a = 1
    b = II()
    while a < b:
        i += 1
        a = (a + 1) * 2
    print(i)
