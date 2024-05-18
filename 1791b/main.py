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
    a = II()
    dir = I()
    l = 0
    r = 0
    flag = False
    for i in dir:
        if l == 1 and r == 1:
            flag = True
        if i == "L":
            l -= 1
        elif i == "R":
            l += 1
        elif i == "U":
            r += 1
        elif i == "D":
            r -= 1
    if l == 1 and r == 1:
        flag = True
    if flag:
        print("YES")
    else:
        print("NO")