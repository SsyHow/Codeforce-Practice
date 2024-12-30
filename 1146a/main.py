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
c = a.count('a')

if len(a) - c >= c:
    print(a.count('a') * 2 - 1)
else:
    print(len(a))
