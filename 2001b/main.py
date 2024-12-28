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
    if b & 1 == 0:
        print(-1)
    else:
        print(*([i for i in range(b, 0, -2)] + [j for j in range(2, b, 2)]), sep = ' ')