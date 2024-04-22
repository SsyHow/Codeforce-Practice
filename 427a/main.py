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
stack = 0
ans = 0

L = LII()
for b in L:
    if stack == 0 and b == -1:
        ans+= 1
    elif b > 0:
        stack += b
    elif b == -1:
        stack -= 1
print(ans)