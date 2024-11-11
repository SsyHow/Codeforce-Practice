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
    L = LII()
    if sum(L) % b:
        print(-1)
        continue
    c = sum(L) // b
    cnt = 0
    for i in L:
        # print(c, i)
        if c < i:
            cnt += 1
    print(cnt)