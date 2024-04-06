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


L = ['I hate ', 'I love '] * 50
a = II()
print('that '.join(L[:a]), 'it', sep='')