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
from collections import Counter

for _ in range(a):
    b = II()
    L = LII()
    dic = {}
    vis = set()
    for idx, i in enumerate(L):
        if i not in dic:
           dic[i] = idx + 1
        else:
            vis.add(i)
    M = sorted(list(set(L)))
    # print(vis, dic)
    for i in M:
        if i in vis:
            continue
        print(dic[i])
        break
    else:
        print(-1)

