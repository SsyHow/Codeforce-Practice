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
for _ in range(a):
    b = II()
    L = sorted(MII())
    mean = L[0]
    for i in L:
        mean = (mean + i) //2
    print(mean)
