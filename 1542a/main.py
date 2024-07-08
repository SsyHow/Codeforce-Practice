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
    cnto, cnte = 0, 0
    for i in L:
        if i % 2:
            cnto += 1
        else:
            cnte += 1
    if b == cnto and b == cnte:
        print("YES")
    else:
        print("NO")