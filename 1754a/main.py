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
    s = I()
    q = ans = 0
    for i in s:
        if i == 'Q':
            q += 1
        else:
            q = max(q - 1, 0)
    if q > 0:
        print("No")
    else:
        print("Yes")
