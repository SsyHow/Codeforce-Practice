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
L = [0 for i in range(a+1)]
for idx, i in enumerate(LII()):
    L[i] = str(idx+1)
L = L[1:]
print(' '.join(L))