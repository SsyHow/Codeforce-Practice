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
b = I()
cnt = 1
p1 = 0
for i in range(len(b)):
    if a[p1] == b[i]:
        p1 += 1
        cnt += 1
print(cnt)