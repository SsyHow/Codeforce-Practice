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
    for i in L:
        if int(i ** 0.5) ** 2 != i:
            print("YES")
            break
    else:
        print("NO")