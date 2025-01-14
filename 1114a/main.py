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

x, y, z = MII()
a, b, c = MII()

A = True if a >= x else False
B = True if b + a - x >= y else False
C = True if b + a - x - y + c >= z else False

print("YES" if A == B == C == True else "NO")