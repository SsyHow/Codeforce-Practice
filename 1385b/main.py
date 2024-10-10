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
for _ in range(a):
    b = I()
    L = set()
    for i in MII():
        if i not in L:
            print(i, end=' ')
            L.add(i)
    print()
