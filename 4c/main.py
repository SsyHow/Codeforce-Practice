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
vis = {}
for _ in range(a):
    x = I()
    if x in vis:
        vis[x] += 1
        print(x, vis[x], sep = '')
    else:
        print("OK")
        vis[x] = 0
