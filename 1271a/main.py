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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = II()
b = II()
c = II()
d = II()
e = II()
f = II()

if e > f:
    k = min(a, d)

    print( k * e + f * (min(d-k, b, c)))
else:
    k = min(b, c, d)

    print(k * f + e * min(d - k, a))