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

a = I()

U, L = 0, 0
for i in a:
    if 'A' <= i <= 'Z':
        U += 1
    else:
        L += 1
if U > L:
    print(a.upper())
else:
    print(a.lower())