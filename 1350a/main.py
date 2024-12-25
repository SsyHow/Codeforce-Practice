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
    x, y = MII()

    div = x
    b = int(x ** 0.5) + 1
    i = 2
    while i < b:
        if x % i == 0:
            div = i
            break
        i += 1
    # print(x, div)
    print(x + div + (y-1) * 2)