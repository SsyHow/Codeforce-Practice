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

for i in range(a):
    if i%2 == 0:
        print("#"*b)
    elif (i+1) % 4 :
        print("."*(b-1), "#", sep='')
    else:
        print("#","."*(b-1), sep='')