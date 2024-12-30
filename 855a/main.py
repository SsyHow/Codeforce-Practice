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
vis = set()
for _ in range(a):
    b = I()
    if b not in vis:
        vis.add(b)
        print("NO")
    else:
        print("YES")