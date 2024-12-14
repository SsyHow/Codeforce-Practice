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

from collections import deque


a = II()
for _ in range(a):
    b = II()
    s = I()
    ans = deque([])
    idx = b
    while idx > 0:
        if s[idx-1] in {'b', 'c', 'd'}:
            ans.appendleft(s[idx-3:idx])
            idx -= 3
        else:
            ans.appendleft(s[idx-2:idx])
            idx -= 2
    print('.'.join(ans))

