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
    fk = 6 - sum(L)
    # print(fk)
    # cnt = 0

    vis = {fk-1}

    while len(vis) < 3 and L[fk-1] - 1 not in vis:
        # print(vis, L[fk-1])
        vis.add(L[fk - 1] - 1)
        fk = L[fk- 1]
        # cnt += 1
        # vis.add(L[fk-1])
    # print(cnt)
    # print(vis)
    if vis == {0,1,2}:
        print("YES")
    else:
        print("NO")