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
for _ in range(a):
    b, c = MII()
    s = I()
    ss = Counter(s)
    ans = 0
    for i in 'ABCDEFG':
        if i not in ss:
            ans += c
        else:
            ans += max((c - ss[i]), 0)
    print(ans)

