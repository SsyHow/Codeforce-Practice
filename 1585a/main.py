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
    prev = 2
    ans = 1
    L = LII()
    for i in L:
        if ans == -1:
            break
        if prev == 1 and i == 1:
            ans += 5
        elif i == 1:
            ans += 1
        elif prev == 0 and i == 0:
            ans = -1
        prev = i
    print(ans)

