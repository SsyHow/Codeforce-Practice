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
    c = I()
    cnt = 0
    for i in c:
        if i == "+":
            cnt += 1
        else:
            cnt -= 1
    print(abs(cnt))