
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
L = LII()
L.sort()
b = II()

def bs(x):
    l, r = 0, a -1

    while l <= r:
        mid = (l + r) // 2
        if L[mid] <= x:
            l = mid + 1
        else:
            r = mid - 1
    return l

for _ in range(b):
    c = II()
    print(bs(c))
