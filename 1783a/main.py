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
    L[0], L[-1] = L[-1], L[0]
    L[-1], L[1] = L[1], L[-1]
    if L[0] == L[1]:
        print("NO")
    else:
        print("YES")
        print(" ".join([str(i) for i in L]))