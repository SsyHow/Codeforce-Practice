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
l = r = 0
for _ in range(a):
    x, y = MII()
    l += 1 if x == 1 else 0
    r += 1 if y == 1 else 0

print(min(l, a - l)+ min(r, a-r))
# print(l, r, a)