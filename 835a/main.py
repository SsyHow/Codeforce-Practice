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

n, v1, v2, t1, t2 = MII()
a = v1 * n + 2 * t1
b = v2 * n + 2 * t2

if a == b:
    print("Friendship")
elif a < b:
    print("First")
else:
    print("Second")