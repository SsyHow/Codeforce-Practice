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
    if b < 10:
        print(b)
        continue
    elif b > 45:
        print(-1)
        continue
    cnt = 9
    s = ''
    while b > 0 :
        s = str(min(b, cnt)) + s

        b -= cnt
        cnt -= 1
    print(s)

