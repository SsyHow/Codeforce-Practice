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

from collections import Counter
a = II()
s = I()
vis = Counter()
for i in range(a-1):
    vis[s[i:i+2]] += 1
print(vis.most_common()[0][0])
