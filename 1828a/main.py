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
    if b % 2 == 1:
        print(*([i for i in range(1, b+1)]), sep = ' ')
    else:
        print(*([i * 2 for i in range(1, b+1)]), sep = ' ')
