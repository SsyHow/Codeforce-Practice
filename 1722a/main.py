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
for i in range(a):
    b = II()
    s = I()
    word = "Timur"

    if b == 5 and Counter(word) == Counter(s):
        print("YES")
    else:
        print("NO")