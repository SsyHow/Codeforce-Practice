
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

for i in range(a):
    a,b = MII()
    a, b = max(a,b), min(a,b)
    print(max(a, b*2) ** 2)