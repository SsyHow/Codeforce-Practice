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

a,b = MII()
flag = False
for i in range(a):

    x = LI()
    if any(l in x for l in {"C", "M", "Y"}):
        flag = True
print("#Color") if flag else print("#Black&White")
