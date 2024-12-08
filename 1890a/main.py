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
    C = list(Counter(LII()).items())

    if len(C) > 2:
        print("NO")
    elif len(C) == 1:
        print("YES")
    else:
        if abs(C[0][1] - C[1][1]) <= 1:

            print("YES")
        else:
            print("NO")
