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
    while len(c) > 1:
        if (c[0] == '1' and c[-1] == '0') or (c[0] == '0' and c[-1] == '1'):
            c = c[1:-1]
        else:
            break
    print(len(c))