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
b = LII()

b.sort()
l, r = 0, len(b)-1

while l < r:
    print(b[l], b[r])
    l += 1
    r -= 1

