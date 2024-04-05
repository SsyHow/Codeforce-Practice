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

k = II()
l = II()
m = II()
n = II()
d = II()

L = [False for _ in range(d)]

M = [k, l, m, n]
# if 1 in M:
#     print(d)
# else:
for i in M:
    a = i
    while a <= d:
        L[a-1] = True
        a += i
        # print(a)
    # L[0] = False
print(sum(L))
