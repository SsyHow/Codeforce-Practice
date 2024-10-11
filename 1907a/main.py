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
    b = I()
    for j in 'abcdefgh':
        if j == b[0]:
            continue
        print(j, b[1], sep='')
    for k in range(1, 9):
        if str(k) == b[1]:
            continue
        print(b[0], k, sep='')
