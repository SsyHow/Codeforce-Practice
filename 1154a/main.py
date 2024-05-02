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

a = max(L)

for i in L:
    if i == a:
        continue
    print(a - i, end = ' ')
print()