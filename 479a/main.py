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
b = II()
c = II()

print(max(a +b +c, a * (b + c), (a + b) * c, a * b * c))