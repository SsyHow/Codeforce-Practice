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

from collections import Counter
a = II()
for _ in range(a):
    b = II()
    L = LII()
    L = Counter(L)
    for i in L:
        if L[2] % 2 == 1 and L[1] == 0:
            print("NO")
            break
        elif L[1] %2 == 1:
            print("NO")
            break
    else:
        print("YES")
