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

from collections import defaultdict
a = II()
for _ in range(a):
    b = II()
    L = LII()
    c = (zip(sorted(L), range(b, 0, -1)))
    dic = defaultdict(list)
    for x, y in c:
        dic[x].append(y)

    for i in L:
        print(dic[i][-1], end = ' ')

        dic[i].pop()
    print()