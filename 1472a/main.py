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
    b,c,d = MII()
    w , h = 1, 1
    while b % 2 == 0:
        b //= 2
        w *= 2
    while c % 2 == 0:
        c //= 2
        h *= 2
    if w * h >= d:
        print("YES")
    else:
        print("NO")