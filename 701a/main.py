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
L = LII()

M = sorted((i, idx+1) for idx, i in enumerate(L))
for i in range(a//2):
    print(M[i][1], M[a-1-i][1])






