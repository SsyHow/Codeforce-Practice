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
    c = Counter(I())

    if len(c) < 2:
        print("NO")
    else:
        c = c.most_common()
        if c[0][1] > 1 and c[1][1] > 1:
            print("YES")
        else:
            print("NO")