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
    s = I()
    cnt = 0
    prev = 1
    for i in s:
        c = int(i)
        if c == 0:
            c = 10

        cnt += abs(prev - c) + 1
        prev = c
    print(cnt)

