# import sys
# sys.setrecursionlimit(1000000)
# input=lambda:sys.stdin.readline().strip()


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

a = II()
for _ in range(a):
    b = II()
    p1, p2 = MII()
    flag = True
    for _ in range(b-1):
        x, y = MII()
        if p1 <= x and p2 <= y:
            flag = False

    print(p1) if flag else print(-1)