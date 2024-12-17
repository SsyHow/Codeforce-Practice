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
    M = LII()
    dif = float('inf')

    for i in range(b):
        if M[i] > 0:
            dif = min(dif, L[i] - M[i])
    if dif < 0:
        print("NO")
    else:
        for i in range(b):
            if L[i] - M[i] > dif:
                print("NO")
                break
        else:
            print("YES")
