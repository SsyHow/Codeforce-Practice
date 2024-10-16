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
    b, k = MII()
    s = I()
    c = 0
    cnt = 0
    while c < b:
        if s[c] == 'B':
            c += k
            cnt += 1
            continue
        c+= 1
    print(cnt)