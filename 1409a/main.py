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
    b,c = MII()
    if abs(b-c) % 10 == 0:
        print(abs(b-c)//10)
    else:
        print(abs(b-c)//10 + 1)
