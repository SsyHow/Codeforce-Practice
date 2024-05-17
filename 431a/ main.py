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

a1, a2, a3, a4 = MII()

L = I()
ans = 0
dic = {"1" : a1, "2": a2, "3": a3, "4": a4}
for i in L:
    ans += dic[i]
print(ans)