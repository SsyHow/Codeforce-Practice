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

k, n, w = MII()

print(max(0, (1+w)*w//2 *k - n))
