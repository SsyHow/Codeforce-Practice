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
for i in range(a):
    b = II()
    L = list(range(2, b + 1)) + [1]
    for i in L:
        print(i, end=' ')
    print()