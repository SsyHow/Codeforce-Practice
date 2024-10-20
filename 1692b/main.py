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
    c = Counter(LII())
    # print(c)
    # if len(c) == 1:
    #     print(0) if b % 2== 0 else print(1)
    # elif len(c) == b:
    #     print(b)
    cnt = 0
    for i in c:
        if c[i] > 1:
            cnt += c[i]-1

    if cnt % 2:
        print(len(c) - 1)
    else:
        print(len(c))