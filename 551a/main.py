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
L = LII()

c = Counter(L)
k = 1
dic = {}
for i in sorted(set(c), reverse=True):
    dic[i] = k
    k += c[i]
# print(dic)
ans = []
for i in L:
    ans.append(dic[i])
print(*ans)









