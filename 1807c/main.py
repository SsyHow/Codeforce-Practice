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
    b = II()
    c = I()
    vis = {}
    for idx, i in enumerate(c):
        if i not in vis:
            vis[i] = idx % 2
        else:
            if idx % 2 == vis[i]:
                continue
            else:
                print("NO")
                break
    else:
        print("YES")
