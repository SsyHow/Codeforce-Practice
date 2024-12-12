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
for _ in range(a):
    b = I()
    L = LII()
    x = min(L)
    L.sort(reverse=True)
    while L and L[-1] == x:
        L.pop()
    # print(L)
    print(len(L))