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
    L = list(range(1, b+1))
    if b == 1:
        print(1)
    elif b == 3:
        print(2,1,3)
    elif b & 1 == 0:
        for i in range(0,b-1,2):

            L[i], L[i+1] = L[i+1], L[i]
        L[-1], L[-2] = L[-2], L[-1]
        print(*L)
    else:
        for i in range(3,b-1,2):
            L[i], L[i+1] = L[i+1], L[i]
        L[-1], L[-2] = L[-2], L[-1]
        print(*L)
