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
if min(a,b) % 2 == 0:
    print("Malvika")
else:
    print("Akshat")