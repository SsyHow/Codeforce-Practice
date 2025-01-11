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
    b = II()
    print(2)
    for i in range(1, b+1):
        if i & 1 > 0:
            j = i
            while j <= b:
                print(j, end = ' ')
                j *= 2
    print()

