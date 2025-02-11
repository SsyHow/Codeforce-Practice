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

# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
a, b = LII()
L = LII()
neg = L.count(-1)
pos = L.count(1)

for _ in range(b):
    x, y = MII()
    k = y - x + 1

    if k & 1 == 0 and neg >= k // 2 and pos >= k //2:
        print(1)
    else:
        print(0)





