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
    b = {'X', 'O', '+'}
    for i in range(3):
        L.append(list(I()))
    for i in range(3):
        if L[i][0] == L[i][1] == L[i][2] and L[i][0] in b:
            print(L[i][0])
            break

        elif L[0][i] == L[1][i] == L[2][i] and L[0][i] in b:
            print(L[0][i])
            break

        elif (L[0][0] == L[1][1] == L[2][2] or L[0][2] == L[1][1] == L[2][0]) and L[1][1] in b:
            print(L[1][1])
            break
    else:
        print("DRAW")


