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
M = LII()

L.sort()

ans = [0] * b
for i in range(b):

    l, r = 0, a - 1

    while l <= r:
        mid = (l + r) //2

        if L[mid] < M[i]+1:
            l = mid + 1
        else:
            r = mid - 1

    ans[i] = l
print(*ans, sep=' ')

