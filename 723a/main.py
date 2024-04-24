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

a = LII()

locmax = max(a)
locmin = min(a)
mid = sum(a) - locmin - locmax

print(locmax - mid + mid - locmin)