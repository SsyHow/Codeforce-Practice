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
    b, c = MII()

    if b == c:
        print(*([1] * b))
    elif c == 1 or b == 1:
        print(*range(1, max(b, c) + 1))
    else:
        print(-1)