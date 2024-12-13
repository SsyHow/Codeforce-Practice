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
L = LII()
for i in range(a):
    if i != 0 and i != a-1:
        print(min(L[i] - L[i-1], L[i+1] - L[i]), max(L[i] - L[0], L[a-1] - L[i]))
    elif i == 0:
        print(L[1] - L[0], L[a-1] - L[0])
    else:
        print(L[a-1] - L[a-2], L[a-1] - L[0])