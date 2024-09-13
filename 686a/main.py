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
cnt = 0
for i in range(a):
    c = LI()
    if c[0] == '+':
        b += int(c[1])
    else:
        if b < int(c[1]):
            cnt += 1
        else:
            b -= int(c[1])
print(b, cnt)
