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
    x, y = MII()
    c = Counter(I())
    flag = True
    if x > 0 and x > c['R']:
        flag = False
    if x < 0 and -x > c['L']:
        flag = False
    if y > 0 and y > c['U']:
        flag = False
    if y < 0 and -y > c['D']:
        flag = False

    if flag:
        print("YES")
    else:
        print("NO")
