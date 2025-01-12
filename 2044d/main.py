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
    vis = set()
    j = 1
    ans = []
    for i in L:
        if i not in vis:
            ans.append(i)
            vis.add(i)
        else:
            while j in vis:
                j += 1
            ans.append(j)
            vis.add(j)
    print(*ans)


