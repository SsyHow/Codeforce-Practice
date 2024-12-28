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
L = LII()
a = min(L)
tmp = float('inf')
for i in L:
    if i > a and i < tmp:
        tmp = i

print(tmp) if tmp != float('inf') else print("NO")