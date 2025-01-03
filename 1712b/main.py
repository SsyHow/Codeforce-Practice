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
    n = II()
    if n & 1 == 0:
        for i in range(1, n+1, 2):
            print(i+1, i, end = ' ')
        # print()
    else:
        print(1)
        for i in range(2, n+1, 2):
            print(i+1, i, end = ' ')
        # print()