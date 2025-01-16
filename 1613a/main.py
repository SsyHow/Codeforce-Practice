import sys
input=lambda:sys.stdin.readline().strip()


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
    x1, p1 = MII()
    x2, p2 = MII()

    mn = min(p1, p2)

    p1 -= mn
    p2 -= mn

    if p1 >= 7:
        print(">")
    elif p2 >= 7:
        print("<")
    else:
        x1 = x1 * (10 ** p1)
        x2 = x2 * (10 ** p2)
        if x1 > x2:
            print(">")
        elif x1 < x2:
            print("<")
        else:
            print("=")