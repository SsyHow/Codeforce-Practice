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
    s = []
    c = b // 2
    for i in range(1, b//2+1):
        s.append(i + c)
        s.append(i)
    if b & 1 == 1:
        s.append(b)

    print(*s)