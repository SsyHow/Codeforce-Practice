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
    s = I()
    vis = set()
    cnt = 0
    for i in s:
        # print(vis)

        if i not in vis:
            if len(vis) == 3:
                vis = set()
                cnt += 1
            vis.add(i)

    print(cnt) if not vis else print(cnt +1)