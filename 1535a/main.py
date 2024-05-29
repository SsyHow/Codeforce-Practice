
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
    L = LII()
    S = sorted(L)
    if (S[0] in L[:2] and S[1] in L[2:]) or (S[0] in L[2:] and S[1] in L[:2]):
        print("YES")
    else:
        print("NO")