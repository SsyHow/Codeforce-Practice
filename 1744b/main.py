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
for i in range(a):
    b, c = MII()
    L = LII()
    odd = even = 0
    ans = sum(L)
    for i in L:
        if i % 2 == 1:
            odd += 1
        else:
            even += 1

    for i in range(c):
        x, y = MII()

        if x == 0:
            ans += even * y
        else:
            ans += odd * y

        if x == 1 and y % 2 == 1:
            odd += even
            even = 0
            even += odd
            odd = 0
        elif x == 0 and y % 2 == 1:
            odd += even
            even = 0
        print(ans)