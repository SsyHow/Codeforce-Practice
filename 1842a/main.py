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
    L1 = sum(LII())
    L2 = sum(LII())

    if L1 == L2:
        print("Draw")
    elif L1 > L2:
        print("Tsondu")
    else:
        print("Tenzing")