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

ans = [0] * 1001
cnt = 1
for i in range(1, 1001):
    ans[i] = cnt
    cnt += 1
    while cnt%10 == 3 or cnt % 3 == 0:
        cnt += 1

for i in range(a):
    n = II()
    print(ans[n])