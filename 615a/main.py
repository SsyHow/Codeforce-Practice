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

a, b = MII()
tmp = set()
for _ in range(a):
    L = LII()
    tmp = tmp.union(set(L[1:]))

if len(tmp) == b:
    print("YES")
else:
    print("NO")