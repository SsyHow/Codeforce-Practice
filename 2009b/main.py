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
    L = []
    for _ in range(b):
        c = I()

        for j in range(4):
            if c[j] == '#':
                L.append(str(j+1))
    print(' '.join(L[::-1]))


