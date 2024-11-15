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

a = I()
L = LII()
c = max(L)
cnt = [0] * (c + 1)
for i in L:
    cnt[i] += 1

# print(cnt)
for i in range(2, c+1):
    cnt[i] = max(cnt[i-1], cnt[i-2] + cnt[i] * i)

print(cnt[-1])

