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
n = 0
cnt = 0
while n <= a:
    cnt += 1
    n += (1 + cnt) * cnt // 2

print(cnt-1)
