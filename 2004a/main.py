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
    if b > 2:
        print("NO")
    else:
        if sum(L)//2 == L[0]:
            print("NO")
        else: print("YES")