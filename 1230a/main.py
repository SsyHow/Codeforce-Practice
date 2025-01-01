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

a, b, c, d = LII()

s = a + b +c+ d
m = max(a,b,c,d)
if s & 1 == 1:
    print("NO")
else:

    i = a + b == s//2 or a + c == s//2 or a + d == s//2 or c + b == s//2 or d + b == s//2 or d + c == s//2 or m == s//2

    print("YNEOS"[1 - i::2])
