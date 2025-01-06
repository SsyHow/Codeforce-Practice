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


a, b = MII()
s = list('qwertyuiopasdfghjklzxcvbnm')

print(''.join(s[:b] * (a//b) + s[:a%b]))