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
for i in range(a):
    b = II()
    if b == 1:
        print(0)
        continue
    if b % 3 :
        print(-1)
        continue
    cnt3, cnt2 = 0, 0
    while b % 3 == 0:
        b //= 3
        cnt3 += 1
    while b % 2 == 0:
        b //= 2
        cnt2 += 1

    if b > 2 :
        print(-1)

    elif cnt2 > cnt3:
        print(-1)

    else:
        print(cnt3 + (cnt3 - cnt2))


