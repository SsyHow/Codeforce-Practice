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


a, k = MII()
joy = float('-inf')
for _ in range(a):
    f, t = MII()
    if t > k:
        joy = max(joy, f - (t - k))
    else:
        joy = max(f, joy)

print(joy)
