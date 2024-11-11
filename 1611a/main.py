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
    if b[-1] in {'2', '4', '6', '8'}:
        print(0)
    elif b[0] in {'2', '4', '6', '8'}:
        print(1)
    elif any(b[i] in {'2', '4', '6', '8'} for i in range(len(b))):
        print(2)
    else:
        print(-1)