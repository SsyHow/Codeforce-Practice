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

L = LII()
M = LII()
c = II()
print("YES") if c >= ((sum(L) + 5 - 1)//5 + (sum(M) + 10 - 1) // 10) else print("NO")