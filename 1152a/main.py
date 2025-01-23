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

a, b = MII()
L1 = LII()
L2 = LII()

o1 = sum(1 for i in L1 if i & 1 == 1)
e1 = a - o1

o2 = sum(1 for i in L2 if i & 1 == 1)
e2 = b - o2

print(min(o1, e2) + min(o2, e1))