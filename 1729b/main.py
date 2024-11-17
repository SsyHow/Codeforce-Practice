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

from collections import deque
a = II()
for _ in range(a):
    b = II()
    c = I()
    a = deque()
    while b > 0:
        b -= 1
        # print(b)
        if c[b] != '0':
            a.appendleft(chr(int(c[b]) + 96))
        else:
            b -= 2
            a.appendleft(chr(int(c[b:b+2]) + 96))
    # print(a)
    print(''.join(a))