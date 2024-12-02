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
    a0 = a1 = 0
    for i in s:
        if i == '1':
            a1 += 1
        else:
            a0 += 1
    print(min(a0,a1)) if a0 != a1 else print(a0-1)