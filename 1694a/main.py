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
    if b >= c:
        print('01' * (c) + '0' * (b-c))
    else:
        print('10' * (b) + '1' * (c-b))