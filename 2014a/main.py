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
    n, k = MII()
    L =LII()
    have = cnt = 0
    for i in L:
        if i >= k:
            have += i
        elif have and i == 0:
            cnt += 1
            have -= 1
    print(cnt)