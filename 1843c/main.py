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
    c = II()
    b = bin(c)[2:]
    cnt = 0
    while b:
        cnt += int(b, 2)
        b = b[:-1]
    print(cnt)
