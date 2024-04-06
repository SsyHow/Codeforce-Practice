import sys
_input = input

def input():
    return sys.stdin.readline()

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
    x, y = MII()
    if x%y == 0:
        print(0)
    else:
        print(y * (x//y + 1) - x)
