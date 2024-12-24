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
    L = []
    L.append([int(i) for i in I()])
    L.append([int(i) for i in I()])
    # print(L)
    for i in range(b-1):
        if L[0][i+1] == L[1][i+1] == 1:
            print("NO")
            break
    else:
        print("YES")