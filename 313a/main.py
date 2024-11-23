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
if int(a) >= 0:
    print(a)
else:
    print(max(int(a[:-1]), int(a[:-2] + a[-1])))