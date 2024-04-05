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

a =I()


if '0000000' in a or '1111111' in a:
    print('YES')
else:
    print('NO')