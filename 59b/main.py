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

b = LII()
b.sort()
c = sum(b)

d = [i for i in b if i % 2]

if c % 2:
    print(c)
else:
    if len(d) == 0:
        print(0)
    else:

        print(c - d[0])

