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
    c = Counter()
    for _ in range(b):
        s = I()
        for i in s:
            c[i] += 1

    for i in c:
        if c[i] % b:
            print("NO")
            break
    else:
        print("YES")