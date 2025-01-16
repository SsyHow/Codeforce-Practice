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

def f(n):
    x = 0
    while n > 0:
        x += n % 10
        n //= 10
    return x

a = II()
for _ in range(a):
    b, c = MII()

    while f(b) % c != 0:
        b += 1
    print(b)