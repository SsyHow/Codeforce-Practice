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
    c = Counter(list(I()))

    for i in c:
        if c[i] == 4:
            print(-1)
            break
        elif c[i] == 3:
            print(6)
            break
    else:
        print(4)