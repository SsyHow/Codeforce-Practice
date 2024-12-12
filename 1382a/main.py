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

    b, c = MII()

    L1 = LII()
    L2 = LII()

    if c > b :
        L1, L2 = L2, L1

    for i in L1:
        if i in L2:
            print(f"YES\n1 {i}")
            break
    else:
        print("NO")