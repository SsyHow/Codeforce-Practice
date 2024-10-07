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
    cnt = 0
    for i in range(10):
        b = I()
        for j in range(10):
            if b[j] == 'X':
                c = min(i, 9-i, j, 9-j)
                c += 1
                cnt += c
    print(cnt)