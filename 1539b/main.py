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

# from collections import Counter
a, b = MII()
s = I()
L = []
tmp = 0
for i in range(a):
    tmp += (ord(s[i]) - ord('a') + 1)
    L.append(tmp)
# print(L)
for i in range(b):
    x, y = MII()
    if x == 1:
        print(L[y-1])
    else:
        print(L[y-1] - L[x-2])
