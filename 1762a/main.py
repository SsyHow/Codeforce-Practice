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
    L = LII()
    L.sort()
    ans = float('inf')
    if sum(L) & 1 == 0:
        print(0)
    else:

        for i in L:
            if i & 1 == 1:
                tmp = 0
                while i & 1 == 1:
                    i //= 2
                    tmp += 1
                ans = min(ans, tmp)
            elif i & 1 == 0:
                tmp = 0
                while i & 1 == 0:
                    i //= 2
                    tmp += 1
                ans = min(ans, tmp)


        print(ans)