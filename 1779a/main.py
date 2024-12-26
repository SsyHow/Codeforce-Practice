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

    if 'RL' in c:
        print(0)
    elif 'LR' in c:
        print(c.index('LR') + 1)
    else:
        print(-1)