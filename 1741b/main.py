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
    L = list(range(1, b+1))[::-1]
    if b == 3:
        print(-1)
        continue
    if b == 5:
        print(3,4,5,1,2)
        continue
    if len(L) % 2 == 1:
        c = len(L)
        L[c//2], L[c//2 + 1] = L[c//2 + 1], L[c//2]
    print(*L, sep=' ')