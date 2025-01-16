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
c = b - 1

print((a*2+c)//b + (a*5 +c) // b + (a*8 + c)//b)