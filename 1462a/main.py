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
    b = II()
    L = LII()
    a = [0] * b

    for i in range(b):
        if i % 2== 0:
            a[i] = str(L[i//2])
        else:
            a[i] = str(L[-(i//2 + 1)])
    # print(a)
    print(' '.join(a))

