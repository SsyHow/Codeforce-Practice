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
    flag = True
    cnt = 1
    for i in range(b):
        s = I()
        if flag:
            for j in range(c):
                if s[j] == '#':
                    x, y = i, j
                    flag = False
        if s.count('#') >= cnt:
            cnt = s.count('#')
            x = i
    print(x+1, y+1)