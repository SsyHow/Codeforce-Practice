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

a, b = MII()
L = LI()
ans = 0
for i in L:
    if i.count('4') + i.count('7') <= b:
        ans += 1
print(ans)