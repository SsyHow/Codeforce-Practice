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
ans = []
vis = set()
L.reverse()
for i in L:
    if i in vis:
        continue
    ans.append(i)
    vis.add(i)
ans.reverse()
print(len(ans))
print(' '.join([str(i) for i in ans]))