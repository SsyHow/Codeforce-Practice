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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

a = II()
for _ in range(a):
    b, c = MII()
    L = []
    for _ in range(b):
        L.append(list(I()))
    ans = [1] * b
    for i in range(c):
        for j in range(b):
            # print(b, c, i, j)
            if ans[j] == 1 and L[j][i] != L[0][i]:
                ans[j] = 0
    print(sum(ans))