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
    if b <= 1399:
        print('Division 4')
    elif b <= 1599:
        print('Division 3')
    elif b <= 1899:
        print('Division 2')
    else:
        print('Division 1')