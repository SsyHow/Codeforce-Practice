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

k2, k3, k5, k6 = MII()
c = min(k2, k5, k6)
print(c * 256 + min(k3, k2 - c) * 32)