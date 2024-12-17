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
c = L[2] - (L[0] + L[1]) + 1
print(c) if c > 0 else print(0)