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
    n = I()

    if int(n) < 10:
        print(n)
    else:
        print(((len(n) - 1) * 10 - (len(n) - 1)) + int(n[0]))

