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
L = []

for _ in range(a):
    L.append(LII())

b = II()
for i in range(a):
    # print(L[i])
    if L[i][0] <= b <= L[i][1]:
        print(a - i)
        break