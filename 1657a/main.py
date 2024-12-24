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
    m, n = MII()
    if m == 0 and n == 0:
        print(0)
    elif ((m ** 2 + n ** 2) ** 0.5).is_integer():
        print(1)
    else:
        print(2)