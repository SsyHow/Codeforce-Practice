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
for _ in range(a):
    b = I()
    c = I()
    vis = set()
    for i in b:
        vis.add(i)
    for i in c:
        vis.add(i)

    print(len(vis) - 1)