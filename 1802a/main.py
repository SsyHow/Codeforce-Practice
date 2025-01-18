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
    L = LII()

    pos = sum([1 if i > 0 else 0 for i in L])
    neg = b-pos
    # print((pos-1, b-neg, -1))
    print(*range(1, pos+1), *range(pos-1, pos - 1 - neg, -1))
    print(*([1, 0] * neg), *range(1, b- neg*2+1))