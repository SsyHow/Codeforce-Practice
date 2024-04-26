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
    c = II()
    L = LII()
    L.sort()
    if any(L[i+1] - L[i] > 1 for i in range(len(L)-1)):
        print('NO')
    else:
        print("YES")
