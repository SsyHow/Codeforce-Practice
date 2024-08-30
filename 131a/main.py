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
case1 = a.upper()
case2 = a[0].lower() + a[1:].upper()

if a == case1:
    print(a.lower())

elif a == case2:
    print(a[0].upper() + a[1:].lower())
else:
    print(a)