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
    L.sort()

    prev = L[0]
    for i in range(b):
        if L[i] != prev:
            print(b - i)
            break
    else:
        print(0)