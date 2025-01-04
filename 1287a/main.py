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
    x = 0
    s = I()
    tmp = 0
    flag = False
    for i in s:
        if i == 'A':
            x = max(x, tmp)
            tmp = 0
            flag = True
        elif flag:
            tmp += 1
    x = max(x, tmp)
    print(x)

