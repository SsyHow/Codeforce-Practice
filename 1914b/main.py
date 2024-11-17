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
    L = list(range(1, b + 1))
    M = L[:c] + L[c:][::-1]
    print(' '.join([str(i) for i in M]))
