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
    a01 = a10 = a11 = float('inf')
    for _ in range(b):
        x, y = input().split()
        if y == '01':
            a01 = min(int(x), a01)
        elif y == '10':
            a10 = min(int(x), a10)
        elif y == '11':
            a11 = min(int(x), a11)
    # print(a01, a10, a11)
    if min(a01 + a10, a11) == float('inf'):
        print(-1)
    else:
        print(min(a01 + a10, a11))
