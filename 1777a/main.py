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
    tmp = cnt = 0
    prev = L[0] % 2
    for i in L:
        if i % 2 == prev:
            tmp += 1
        else:
            cnt += tmp - 1
            prev = 1 - prev
            tmp = 1
    cnt += tmp - 1 if tmp > 1 else 0
    print(cnt)