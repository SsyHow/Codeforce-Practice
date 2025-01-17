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
m = 0

ans = []
for i in L:
    tmp = i + m
    ans.append(tmp)
    if i > 0 :
        m = tmp
print(*ans)


