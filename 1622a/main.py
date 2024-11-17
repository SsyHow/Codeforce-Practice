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
    L = LII()
    if sum(L) % 2 == 1:
        print("NO")
    else:
        L.sort()
        if L[0] + L[1] == L[2]:
            print("YES")
        elif L[0] == L[1] or L[1] == L[2]:
            print("YES")
        else:
            print("NO")