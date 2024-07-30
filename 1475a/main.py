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
    while b % 2 == 0:
        b //= 2
    if b != 1:

        print("YES")
    else:
        print("NO")