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
    n, c0, c1, h = MII()
    s = I()

    zero = ones = 0

    for i in s:
        if i == '1':
            ones += 1
        else:
            zero += 1
    if c0 > c1 + h:
        ans = n * c1 + h * zero
    elif c1 > c0 + h:
        ans = n * c0 + h * ones
    else:
        ans = c1 * ones + c0 * zero
    print(ans)