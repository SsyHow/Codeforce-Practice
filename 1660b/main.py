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
    b = II()
    L = LII()

    if b == 1:
        if L[0] > 1:
            print("NO")
            continue
        else:
            print("YES")
            continue
    L.sort()
    if L[-1] - L[-2] >= 2:
        print("NO")
    else:
        print("YES")