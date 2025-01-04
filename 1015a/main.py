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

a, n = MII()
k = []
ans = []
for _ in range(a):
    k.append(LII())
for i in range(1, n+1):
    flag = True
    for x, y in k:
        if x <= i <= y:
            flag = False
            break
    if flag:
        ans.append(i)

print(len(ans))
print(*ans)