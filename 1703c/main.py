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
    for i in range(b):
        _, k = I().split()
        c = 0
        for j in k:
            if j == 'D':
                c += 1
            else:
                c -= 1
        L[i] = str((L[i] + c) % 10)
    print(' '.join(L))