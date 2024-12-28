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
    if b % 3 == 1:
        print('1' + '21' * (b // 3))
    elif b % 3 == 2:
        print('2' + '12' * (b // 3))
    else:
        print('21' * (b // 3))