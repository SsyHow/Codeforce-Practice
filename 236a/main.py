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

a = I()

if len(set(a)) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
