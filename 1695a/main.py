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
    b, c = MII()
    maxm, ki, kj = float('-inf'), 0, 0
    for i in range(b):
        k = LII()
        if maxm < max(k):
            maxm, ki, kj = max(k), i, k.index(max(k))

    print(max(ki+1, b-ki) * max(kj+1, c-kj))



