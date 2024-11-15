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

from math import sqrt,ceil

a = II()
for _ in range(a):
    b = II()
    # L = [0] * (b+1)
    cnt = set()
    for i in range(1, b+1):

        if i ** 2 > b:
            break
        cnt.add(i**2)
        if i ** 3 <= b:
            cnt.add(i**3)

    # print(cnt)
    print(len(cnt))