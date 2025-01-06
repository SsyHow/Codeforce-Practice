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
    b,c = MII()
    L = LII()
    dic = defaultdict(list)
    for idx, i in enumerate(L):
        dic[i%c].append(idx)

    for i in dic:
        if len(dic[i]) == 1:
            print("YES")
            print(dic[i][0]+1)
            break
    else:
        print("NO")