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

    dic = defaultdict(int)
    ans = 0
    for idx, x in enumerate(L):

        x -= idx
        ans += dic[x]
        dic[x] += 1
    print(ans)
