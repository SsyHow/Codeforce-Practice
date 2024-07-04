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
n = len(a)
ql = [0] * n
qr = [0] * n
count = 0
for i in range(n):
    if a[i] == "Q":
        count += 1
    ql[i] = count
count = 0
for i in range(n-1, -1, -1):
    if a[i] == "Q":
        count += 1
    qr[i] = count
ans = 0
# print(ql)
# print(qr)
for i in range(n):
    if a[i] == "A":
        ans += ql[i] * qr[i]
print(ans)