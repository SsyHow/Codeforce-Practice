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
    b, c = MII()
    cnt = 0
    for i in range(b):
        s = I()
        if s[-1] == 'R':
            cnt += 1

        if i == b-1:
            cnt += s.count('D')
    print(cnt)