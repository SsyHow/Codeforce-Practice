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
    b = I()
    if b[0] == b[2]:
        print(f'{b[0]}={b[2]}')
    elif b[0] > b[2]:
        print(f'{b[0]}>{b[2]}')
    else:
        print(f'{b[0]}<{b[2]}')