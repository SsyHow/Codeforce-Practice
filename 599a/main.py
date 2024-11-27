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

L = LII()
L.sort()
if L[2] < L[0] + L[1]:
    print(sum(L))
else:
    print(2 * (L[0] + L[1]))