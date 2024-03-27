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
b = I()
ans = 0
for i in range(a -1 ):
    if b[i] == b[i+1]:
        ans += 1
print(ans)