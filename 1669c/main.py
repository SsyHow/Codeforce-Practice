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
for i in range(a):
    b = II()
    L = LII()
    if b == 2:
        print("YES")
        continue

    x = L[0] % 2
    y = L[1] % 2

    for j in range(b):
        if j % 2 and L[j] % 2 != y:
            print("NO")
            break
        if j % 2 == 0 and L[j] % 2 != x:
            print("NO")
            break
    else:
        print("YES")