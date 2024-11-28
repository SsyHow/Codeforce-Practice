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
    x,y = MII()
    L = LII()
    if len(L) == 1:
        print(0)
    else:
        L.sort()
        prev = float('-inf')
        coll = []
        cnt = 0
        for i in L:
            if i - prev > y:
                coll.append(cnt)
                cnt = 1
            else:
                cnt += 1
            prev = i
        if cnt:
            coll.append(cnt)
        print(sum(coll) - max(coll))