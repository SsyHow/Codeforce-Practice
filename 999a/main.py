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
l, r = 0, a - 1

while l <= r and L[l] <= b:
    l += 1
while l <= r and L[r] <= b:
    r -= 1

print(a - (r - l + 1))
