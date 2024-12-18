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
    x, y = MII()

    L = LII()
    L.sort()
    for i in range(x):
        if L[i + x] - L[i] < y:
            print("NO")
            break
    else:
        print("YES")