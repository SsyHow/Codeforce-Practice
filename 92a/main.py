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

c = b % ((a + 1) * a // 2 )
i = 1
# print(c)
while i <= c:
    # print(i, c)
    c -= i
    i += 1
print(c)