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

for i in range(b):
    if  a%10:
        a -= 1
    else:
        a //= 10
print(a)