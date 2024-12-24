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
    s = I()
    for i in s:
        if i == '1':
            print(13)
            break
        elif i == '3':
            print(31)
            break