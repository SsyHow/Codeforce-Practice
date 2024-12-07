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
    L = []
    cnt = 8
    while cnt > 0:
        c = list(I())
        if c:
        # print(c)
            L.append(c)
            cnt -= 1
    # print(L, len(L), len(L[0]))
    for i in range(8):
        if L[i].count('R') == 8:
            # print(i)
            print("R")
            break


        if all(L[j][i] == 'B' for j in range(8)):
            print("B")
            break
