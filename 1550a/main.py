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
    if b == 1:
        print(1)
    else:
        n = 72
        for i in range(1, n+1):
            # low = ((i+1) * i)//2 - 1
            upp = i * i
            # print(low, upp)
            if b <= upp:
                print(i)
                break