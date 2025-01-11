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
    b,c = MII()
    L = LII()
    if sum(L) == c:
        print("NO")
        continue
    print("YES")
    tmp = 0
    j = 0
    for i in range(b):
        # print(tmp + L[i] == c)

        if tmp + L[i] == c:
            # print(L)
            L[i], L[i+1] = L[i+1], L[i]
            # print(L)
        # print(L)
        tmp += L[i]
        # print(tmp)
    print(*L)
