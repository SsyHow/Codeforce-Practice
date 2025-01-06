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

ans = 0
vis = set()
tmp = 0
for i in L:
    if i not in vis:
        vis.add(i)
        tmp += 1

    else:
        tmp -= 1

    ans = max(tmp, ans)
print(ans)

