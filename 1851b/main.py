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
    M = sorted(L)
    for i in range(b):
        if L[i] % 2 != M[i] % 2:
            print("NO")
            break
    else:
        print("YES")