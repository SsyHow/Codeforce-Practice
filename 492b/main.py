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
L = LII()
L.sort()

maxlist = max([L[i+1] - L[i] for i in range(a-1)]) if len(L) > 1 else 0

print(max(maxlist/2, L[0], b - L[-1]))