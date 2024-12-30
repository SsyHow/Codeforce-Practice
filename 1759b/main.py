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
    x, y = MII()
    L = LII()
    y += sum(L)
    sm = 0
    cnt = 0
    for i in range(1, y+1):
        if sm >= y:
            break
        sm += i
        cnt = i
    if sm!= y or max(L) > cnt or cnt <= x:
        print("NO")
    else:
        print("YES")