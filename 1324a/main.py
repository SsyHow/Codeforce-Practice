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

    k = L[0]

    for i in L:
        if (i - k) % 2 != 0:
            print("NO")
            break
    else:
        print("YES")