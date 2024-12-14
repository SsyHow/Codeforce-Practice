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

L = []
for _ in range(3):
    L.append(LII())
M = [['1' for _ in range(3)] for _ in range(3) ]
for i in range(3):
    for j in range(3):
        num = L[i][j]
        if i > 0:
            num += L[i-1][j]
        if i < 2:
            num += L[i+1][j]
        if j > 0:
            num += L[i][j-1]
        if j < 2:
            num += L[i][j+1]

        if num % 2 == 1:
            M[i][j] = '0'
# print(M)
for i in M:
    print(''.join(i))