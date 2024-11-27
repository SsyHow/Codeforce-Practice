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
    L = LII()
    flag = False
    cnt = 0
    num = 0
    for i in L:
        if i > 0:
            if flag == True:
                num += 1
                flag = False
            cnt += i
        elif i < 0 :
            flag = True
            cnt += -i
    if flag == True:
        num += 1
    print(cnt, num)

